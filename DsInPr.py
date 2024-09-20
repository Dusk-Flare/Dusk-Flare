import os
import shutil
import subprocess

theme_file = r"C:\Windows\Resources\Themes"
destination_folder = r"D:\Themes"

def copy_theme_file(theme_file, destination_folder):
    """
    Copy the .theme file to the appropriate Themes directory in the user's LocalAppData.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.copy2(theme_file, destination_folder)
        print(f"Copied {theme_file} to {destination_folder}")
    except Exception as e:
        print(f"Error copying theme file: {e}")

def copy_wallpapers(source_folder, destination_folder):
    """
    Copy the wallpapers to the Themes directory.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
        print(f"Copied wallpapers from {source_folder} to {destination_folder}")
    except Exception as e:
        print(f"Error copying wallpapers: {e}")

def apply_theme(theme_file):
    """
    Apply the theme by opening the .theme file with Windows settings.
    """
    theme_path = os.path.join('C:\\Windows\\Resources\\Themes', theme_file)
    if os.path.exists(theme_path):
        try:
            # Use 'start' to open the .theme file which applies the theme
            subprocess.run(['start', theme_path], shell=True)
            print(f"Applied theme: {theme_file}")
        except Exception as e:
            print(f"Error applying theme: {e}")
    else:
        print(f"Theme file not found: {theme_path}")

def main():
    theme_file = "dark.theme"  # Replace with your actual .theme file name
    wallpapers_folder = r"wallpapers"    # Replace with your wallpapers folder name (if any)
    
    # Get the destination directories
    themes_dir = os.path.join('C:\\Windows\\Resources\\Themes')
    wallpapers_dest_dir = os.path.join(themes_dir, 'wallpapers')

    # Copy the theme file
    copy_theme_file(theme_file, themes_dir)

    # Copy wallpapers (if available)
    if os.path.exists(wallpapers_folder):
        copy_wallpapers(wallpapers_folder, wallpapers_dest_dir)

    # Apply the theme
    apply_theme(theme_file)

if __name__ == "__main__":
    main()
