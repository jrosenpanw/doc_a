import os
import re
import argparse
import pypandoc

# --- UTILITY FUNCTIONS ---

def sanitize_filename(name):
    """Sanitizes a string to be used as a valid filename."""
    name = re.sub(r'^[#\s]+', '', name).strip()
    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    name = re.sub(r'[-\s]+', '-', name)
    return name

# --- CORE LOGIC: CHUNK MODE ---

def chunk_docx_to_files(docx_path, output_dir, split_level=2):
    """
    Converts a DOCX file to Markdown and splits it into multiple files
    based on headings. (Mode 1)
    """
    print(f"🚀 Running in CHUNK mode: DOCX -> Multiple Markdown files.")
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"🔄 Converting '{os.path.basename(docx_path)}' to Markdown in memory...")
        markdown_content = pypandoc.convert_file(docx_path, 'markdown', format='docx')
        print("✅ In-memory conversion complete.")

        heading_pattern = f"^(?={'#' * split_level}\s)"
        chunks = re.split(heading_pattern, markdown_content, flags=re.MULTILINE)

        if chunks[0].strip():
            intro_path = os.path.join(output_dir, "000-introduction.md")
            with open(intro_path, 'w', encoding='utf-8') as f:
                f.write(chunks[0])
            print(f"📄 Created introduction file: '{intro_path}'")
        
        file_counter = 1
        for chunk in chunks[1:]:
            if not chunk.strip():
                continue
            first_line = chunk.splitlines()[0]
            base_filename = sanitize_filename(first_line)
            filename = f"{file_counter:03d}-{base_filename[:50]}.md"
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(chunk)
            print(f"📄 Created chunk file: '{filename}'")
            file_counter += 1

        print(f"\n🎉 Successfully chunked document into {file_counter - 1} files in '{output_dir}'")
    except OSError:
        print(f"❌ Error: Pandoc not found. Please ensure Pandoc is installed and in your system's PATH.")
    except Exception as e:
        print(f"❌ An error occurred during chunking: {e}")

# --- CORE LOGIC: MERGE MODE ---

def merge_markdown_to_file(source_dir, output_file):
    """
    Merges all markdown files from a directory into a single, structured file,
    adding metadata for better LLM comprehension. (Mode 2)
    """
    print(f"🚀 Running in MERGE mode: Multiple Markdown files -> Single Markdown file.")
    markdown_files = []
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                markdown_files.append(os.path.join(dirpath, filename))
    
    markdown_files.sort() # Sort alphabetically to ensure consistent order

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            print(f"✍️ Merging {len(markdown_files)} files into '{output_file}'...")
            for file_path in markdown_files:
                relative_path = os.path.relpath(file_path, source_dir)
                
                # This header is CRITICAL for the LLM. It provides context and traceability.
                outfile.write(f"---\n")
                outfile.write(f"Source File: {relative_path.replace(os.sep, '/')}\n")
                outfile.write(f"---\n\n")

                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                
                outfile.write("\n\n") # Add space before the next file's header
        print(f"\n🎉 Successfully merged all files into '{output_file}'")
    except Exception as e:
        print(f"❌ An error occurred during merging: {e}")

# --- CONTROLLER ---

def process_documentation(source_dir, output_path):
    """
    Inspects the source directory and decides whether to run in
    CHUNK or MERGE mode.
    """
    print(f"📂 Inspecting source directory: '{source_dir}'")
    if not os.path.isdir(source_dir):
        print(f"❌ Error: Source directory '{source_dir}' not found.")
        return

    docx_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.docx')]
    md_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.md')]

    print(f"🔍 Found {len(docx_files)} DOCX file(s) and {len(md_files)} Markdown file(s).")

    # --- Mode Decision Logic ---
    if len(docx_files) == 1 and not md_files:
        # Case 1: Single DOCX found. Run CHUNK mode.
        # Output should be a directory.
        if os.path.splitext(output_path)[1]: # Check if output_path looks like a file
             print("❌ Error: For CHUNK mode, the output path must be a directory, not a file.")
             return
        chunk_docx_to_files(os.path.join(source_dir, docx_files[0]), output_path)
    
    elif len(md_files) > 0 and not docx_files:
        # Case 2: Markdown files found. Run MERGE mode.
        # Output should be a file.
        if not os.path.splitext(output_path)[1]: # Check if output_path looks like a directory
            print("❌ Error: For MERGE mode, the output path must be a file, not a directory.")
            return
        merge_markdown_to_file(source_dir, output_path)
    
    elif not docx_files and not md_files:
        print("🤷 No source files (.docx or .md) found to process. Exiting.")
    
    else:
        # Ambiguous State
        print("❌ Error: Ambiguous source directory. Found both DOCX and Markdown files.")
        print("👉 Please ensure the source directory contains EITHER one '.docx' file OR multiple '.md' files, but not both.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A smart documentation processor for LLMs. Automatically chunks a DOCX or merges Markdown files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("source_dir", help="Directory containing the source documentation.")
    parser.add_argument(
        "output_path",
        help="The output destination.\n"
             "- For CHUNK mode (input is .docx), this is the OUTPUT DIRECTORY.\n"
             "- For MERGE mode (input is .md), this is the OUTPUT FILE."
    )
    args = parser.parse_args()
    process_documentation(args.source_dir, args.output_path)
