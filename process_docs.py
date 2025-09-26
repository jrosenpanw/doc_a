import os
import re
import argparse
from typing import List, Optional

try:
    import pypandoc
except ImportError:
    pypandoc = None


# --- UTILITY FUNCTIONS ---

def sanitize_filename(name: str) -> str:
    """Sanitizes a string to be used as a valid filename."""
    name = re.sub(r'^[#\s]+', '', name).strip()
    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    name = re.sub(r'[-\s]+', '-', name)
    name, _ = os.path.splitext(name)
    return name


# --- DOCX PROCESSING LOGIC ---

def chunk_docx_to_files(docx_path: str, output_dir: str, split_level: int = 2) -> bool:
    """Converts a single DOCX and splits it into many smaller MD files."""
    if not pypandoc:
        print("❌ Error: pypandoc is not installed. Please run 'pip install pypandoc'.")
        return False
    try:
        base_doc_name = os.path.basename(docx_path)
        print(f"📄 Processing and chunking '{base_doc_name}'...")
        os.makedirs(output_dir, exist_ok=True)
        markdown_content = pypandoc.convert_file(docx_path, 'markdown', format='docx')

        heading_pattern = rf"^(?={'#' * split_level}\s)"
        chunks = re.split(heading_pattern, markdown_content, flags=re.MULTILINE)

        if chunks[0].strip():
            intro_path = os.path.join(output_dir, "000-introduction.md")
            with open(intro_path, 'w', encoding='utf-8') as f: f.write(chunks[0])

        file_counter = 1
        for chunk in chunks[1:]:
            if not chunk.strip(): continue

            # --- THIS IS THE FIX ---
            # The line that prepended extra hashes has been removed.
            # The 'chunk' variable already correctly contains the heading.

            first_line = chunk.splitlines()[0]
            base_filename = sanitize_filename(first_line)
            filename = f"{file_counter:03d}-{base_filename[:50]}.md"
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(chunk)  # We now write the 'chunk' directly
            file_counter += 1
        print(f"✅ Finished '{base_doc_name}', created {file_counter - 1} chunk files in '{output_dir}'.")
        return True
    except OSError:
        print("❌ Error: Pandoc not found. Please ensure Pandoc is installed and in your system's PATH.")
        return False
    except Exception as e:
        print(f"❌ An error occurred while processing {base_doc_name}: {e}")
        return False


def consolidate_docx_to_file(source_dir: str, docx_files: List[str], output_file: str) -> None:
    """Converts multiple DOCX files and consolidates them into a single MD file."""
    if not pypandoc:
        print("❌ Error: pypandoc is not installed. Please run 'pip install pypandoc'.")
        return
    print(f"🚀 Running in DOCX CONSOLIDATE mode for {len(docx_files)} document(s).")

    full_content = ""
    for docx_file in sorted(docx_files):
        print(f"   - Converting '{docx_file}'...")
        file_path = os.path.join(source_dir, docx_file)
        try:
            markdown_content = pypandoc.convert_file(file_path, 'markdown', format='docx')
            full_content += f"\n\n---\n\n# Source Document: {docx_file}\n\n---\n\n"
            full_content += markdown_content
        except Exception as e:
            print(f"❌ Failed to convert {docx_file}: {e}")
            continue

    try:
        output_dir = os.path.dirname(output_file)
        if output_dir: os.makedirs(output_dir, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"\n🎉 Successfully consolidated all DOCX files into '{output_file}'.")
    except Exception as e:
        print(f"❌ An error occurred while writing the output file: {e}")


# --- MARKDOWN MERGE LOGIC ---

def merge_markdown_to_file(source_dir: str, output_file: str) -> None:
    """Merges all markdown files from a directory into a single file."""
    print("🚀 Running in simple MD MERGE mode -> Single large file.")
    markdown_files = sorted(
        [os.path.join(dp, f) for dp, dn, fn in os.walk(source_dir) for f in fn if f.lower().endswith(".md")])
    if not markdown_files:
        print("🤷 No markdown files found to merge.")
        return
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            print(f"✍️ Merging {len(markdown_files)} files into '{output_file}'...")
            for file_path in markdown_files:
                relative_path = os.path.relpath(file_path, source_dir)
                outfile.write(f"---\nSource File: {relative_path.replace(os.sep, '/')}\n---\n\n")
                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                outfile.write("\n\n")
        print(f"\n🎉 Successfully merged all files into '{output_file}'")
    except Exception as e:
        print(f"❌ An error occurred during merging: {e}")


def run_merge_and_split_mode(source_dir: str, output_base_path: str, max_size_mb: int) -> None:
    """Controller for the advanced merge-and-split functionality."""
    print("🚀 Running in MD MERGE mode with intelligent splitting.")
    markdown_files = sorted(
        [os.path.join(dp, f) for dp, dn, fn in os.walk(source_dir) for f in fn if f.lower().endswith(".md")])
    if not markdown_files: return
    full_content = ""
    for file_path in markdown_files:
        relative_path = os.path.relpath(file_path, source_dir)
        header = f"---\nSource File: {relative_path.replace(os.sep, '/')}\n---\n\n"
        with open(file_path, "r", encoding="utf-8") as infile: full_content += header + infile.read() + "\n\n"
    output_dir = os.path.dirname(output_base_path) or '.';
    name_root, name_ext = os.path.splitext(os.path.basename(output_base_path));
    os.makedirs(output_dir, exist_ok=True)
    toc_entries = parse_toc_from_content(full_content)
    if toc_entries:
        print(f"ℹ️ Found ToC. Splitting by document structure.");
        split_by_toc(full_content, toc_entries, output_dir, name_root, name_ext)
    else:
        print(f"ℹ️ No ToC found. Falling back to size-based splitting.");
        split_by_size(full_content, max_size_mb, output_dir, name_root, name_ext)


def parse_toc_from_content(content: str) -> List[str]:
    """Parses a markdown document to find a ToC and returns a list of heading titles."""
    toc_regex = re.compile(r"^\s*[\*\-]\s+\[([^\]]+)\]\s*\(");
    toc_headings = [match.group(1).strip() for line in content.splitlines()[:150] if (match := toc_regex.match(line))];
    return toc_headings if len(toc_headings) > 2 else []


def split_by_toc(content: str, toc_headings: List[str], output_dir: str, name_root: str, name_ext: str) -> None:
    """Splits the full content based on the headings found in the ToC."""
    split_pattern = '|'.join(re.escape(h) for h in toc_headings);
    heading_regex = re.compile(rf"^(#+\s+)({split_pattern})$", re.MULTILINE | re.IGNORECASE);
    chunks = heading_regex.split(content);
    file_counter = 0
    if chunks[0].strip():
        filename = f"{file_counter:02d}-preface{name_ext}";
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f: f.write(chunks[0]); print(
            f"   ✓ Created: {filename}"); file_counter += 1
    for i in range(1, len(chunks), 3):
        full_heading = chunks[i] + chunks[i + 1];
        chunk_content = chunks[i + 2];
        filename = f"{file_counter:02d}-{sanitize_filename(chunks[i + 1])}{name_ext}"
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f: f.write(
            full_heading + chunk_content); print(f"   ✓ Created: {filename}"); file_counter += 1
    print(f"\n🎉 Split into {file_counter} files based on ToC.")


def split_by_size(content: str, max_size_mb: int, output_dir: str, name_root: str, name_ext: str) -> None:
    """Fallback function to split the content by size if no ToC is found."""
    print(f"   - Max file size: {max_size_mb} MB.");
    max_size_bytes = max_size_mb * 1024 * 1024;
    chunks = re.split(r'(---\nSource File:.*?\n---\n\n)', content);
    grouped_chunks = [chunks[0]] + [chunks[i] + chunks[i + 1] for i in range(1, len(chunks), 2)];
    part_counter = 1;
    current_size = 0;
    outfile = None;
    files_created = 0
    for chunk in grouped_chunks:
        if not chunk.strip(): continue
        chunk_size = len(chunk.encode('utf-8'))
        if outfile is None or (current_size + chunk_size > max_size_bytes and current_size > 0):
            if outfile: outfile.close()
            first_heading_match = re.search(r'^#+\s+(.*)', chunk, re.MULTILINE);
            context = f"-{sanitize_filename(first_heading_match.group(1))[:50]}" if first_heading_match else "";
            filename = f"{name_root}_part_{part_counter:02d}{context}{name_ext}";
            filepath = os.path.join(output_dir, filename);
            print(f"✍️ Creating part: {os.path.basename(filepath)}");
            outfile = open(filepath, 'w', encoding='utf-8');
            current_size = 0;
            part_counter += 1;
            files_created += 1
        outfile.write(chunk);
        current_size += chunk_size
    if outfile: outfile.close()
    print(f"\n🎉 Split into {files_created} parts by size.")


# --- CONTROLLER ---

def process_documentation(source_dir: str, output_path: str, max_size: Optional[int] = None,
                          consolidate: bool = False) -> None:
    """Inspects the source directory and decides which mode to run."""
    print(f"📂 Inspecting source directory: '{source_dir}'")
    if not os.path.isdir(source_dir):
        print(f"❌ Error: Source directory '{source_dir}' not found.");
        return

    docx_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.docx')]
    md_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.md')]
    print(f"🔍 Found {len(docx_files)} DOCX file(s) and {len(md_files)} Markdown file(s).")

    if docx_files and not md_files:
        if consolidate:
            if not os.path.splitext(output_path)[1]:
                print("❌ Error: For --consolidate mode, the output path must be a file (e.g., 'output.md').");
                return
            consolidate_docx_to_file(source_dir, docx_files, output_path)
        else:
            if os.path.splitext(output_path)[1]:
                print(
                    "❌ Error: For CHUNK mode, the output path must be a directory. Use --consolidate for a single file output.");
                return
            success_count = sum(1 for docx_file in docx_files if
                                chunk_docx_to_files(os.path.join(source_dir, docx_file),
                                                    os.path.join(output_path, sanitize_filename(docx_file))))
            print(f"\n🎉 Finished processing. Successfully chunked {success_count} of {len(docx_files)} documents.")

    elif md_files and not docx_files:
        if not os.path.splitext(output_path)[1]:
            print("❌ Error: For MERGE mode, the output path must be a file (e.g., 'output.md').");
            return
        if max_size is not None and max_size > 0:
            run_merge_and_split_mode(source_dir, output_path, max_size)
        else:
            merge_markdown_to_file(source_dir, output_path)

    elif not docx_files and not md_files:
        print("🤷 No source files (.docx or .md) found to process.");
        return
    else:
        print("❌ Error: Ambiguous source directory. Found both DOCX and Markdown files.");
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A smart documentation processor. Chunks or consolidates DOCX, or merges MD files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("source_dir", help="Directory containing the source documentation.")
    parser.add_argument("output_path",
                        help="The output destination.\n- DIR for DOCX chunking.\n- FILE for all other modes.")
    parser.add_argument(
        "--max-size",
        type=int,
        help="Optional (MD Mode): Enables splitting. Specifies the max file size in MB."
    )
    parser.add_argument(
        "--consolidate",
        action="store_true",
        help="Optional (DOCX Mode): Consolidate all DOCX files into a single Markdown file."
    )
    args = parser.parse_args()
    process_documentation(args.source_dir, args.output_path, args.max_size, args.consolidate)