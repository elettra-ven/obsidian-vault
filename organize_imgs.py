import os, re, shutil

VAULT_PATH = r"C:\Users\even2\Desktop\elly\elly's digital garden"
IMG_FOLDER_NAME = "img"
IMG_DIR = os.path.join(VAULT_PATH, IMG_FOLDER_NAME)

os.makedirs(IMG_DIR, exist_ok=True)

obsidian_img_pattern = re.compile(r'!\[\[(.*?)(\|.*?)?\]\]')

def organize_vault():
    md_files = []
    referenced_images = set()

    for root, dirs, files in os.walk(VAULT_PATH):
        if IMG_FOLDER_NAME in dirs:
            dirs.remove(IMG_FOLDER_NAME)
            
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                md_files.append(md_path)

                with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                matches = obsidian_img_pattern.findall(content)

                for match in matches:
                    img = match[0].strip()
                    img_name = os.path.basename(img)
                    referenced_images.add(img_name)

    found_images_map = {}
    for root, dirs, files in os.walk(VAULT_PATH):
        if os.path.commonpath([root, IMG_DIR]) == IMG_DIR and root != VAULT_PATH:
            continue
            
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext == '.png':
                img_path = os.path.join(root, file)
                if not img_path.startswith(IMG_DIR):
                    found_images_map[file] = img_path

    for img_name, old_path in found_images_map.items():
        destination_path = os.path.join(IMG_DIR, img_name)
        if not os.path.exists(destination_path):
            shutil.move(old_path, destination_path)
        else:
            os.remove(old_path)

    for md_path in md_files:
        with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        def replace_link(match):
            full_match = match[0]
            raw_target = match[1].strip()
            pipe_params = match[2] if match[2] else ""
            
            img_name = os.path.basename(raw_target)
            if img_name in referenced_images:
                return f"![[{IMG_FOLDER_NAME}/{img_name}{pipe_params}]]"
            return full_match

        update_pattern = re.compile(r'!\[\[(.*?)(\|.*?)?\]\]')
        new_content = update_pattern.sub(replace_link, content)

        if new_content != content:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    for file in os.listdir(IMG_DIR):
        file_path = os.path.join(IMG_DIR, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            if ext == ".png":
                if file not in referenced_images:
                    os.remove(file_path)

if __name__ == "__main__":
    organize_vault()
    print("Fin.")