import os


def create_images_dir(new_dir: str = ""):
    try:
        NAME_NEW_DIR = "images_compression"
        ROOT_DIR = os.getcwd()
        ACTUAL_DIR = ROOT_DIR.split("/")[-1]
        IMAGE_COMPRESSION_DIR = os.path.join(ROOT_DIR, NAME_NEW_DIR)
        name_actual_dir = ""
        for index, dir in enumerate(new_dir.split("/")):
            if dir == ACTUAL_DIR:
                name_actual_dir = new_dir.split("/")[index + 1]
                name_actual_dir = new_dir.replace(name_actual_dir, NAME_NEW_DIR)
        if new_dir == "":
            os.mkdir(IMAGE_COMPRESSION_DIR)
        else:
            os.mkdir(name_actual_dir)
    except FileExistsError:
        print("-------- File already exist!!!")


def file_tracker(content: list[str], path_images: str) -> None:
    for file in content:
        if os.path.isdir(os.path.join(path_images, file)):
            my_dir = file
            actual_path = os.path.join(path_images, my_dir)
            actual_content = os.listdir(actual_path)
            create_images_dir(actual_path)
            file_tracker(content=actual_content, path_images=actual_path)
        if os.path.isfile(os.path.join(path_images, file)):
            print(file)


def image_compression(dir_image: str) -> None:
    try:
        path_images = os.path.join(os.getcwd(), f"{dir_image}")
        actual_path_image = path_images.split("/")
        content = os.listdir(path_images)
        create_images_dir()
        print(f"-------- {actual_path_image[-1]}")
        file_tracker(content, path_images)
        print("Finished work!!!")
    except FileNotFoundError:
        print("Directorio no encontrado o no es valido.")


if __name__ == "__main__":
    image_compression("testDir")
