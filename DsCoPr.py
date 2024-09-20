import subprocess
import os






def create_ddf_file(Compactor, CGT, files_to_include):
    """



    Create a .ddf file with the specified files for the .cab creation.
    """



    with open(Compactor, 'w') as ddf:



        ddf.write(f'.Set CabinetNameTemplate={CGT}\n')



        ddf.write('.Set DiskDirectoryTemplate=.\n')



        ddf.write('.Set Compress=ON\n')



        ddf.write('.Set Cabinet=ON\n')



        ddf.write('.Set DiskDirectory1=.\n')
        



        # Add each file to the DDF



        for file in files_to_include:



            ddf.write(f'"{file}"\n')




    print(f"Created {Compactor} for packaging {CGT}")




def run_makecab(ddf_filename):
    """



    Run the makecab tool with the given .ddf file.
    """



    try:



        subprocess.run(['makecab', '/f', ddf_filename], check=True)



        print(f"Successfully created CAB file using {ddf_filename}")



    except subprocess.CalledProcessError as e:



        print(f"Error while running makecab: {e}")



    except FileNotFoundError:



        print("makecab tool not found. Ensure it's available on the system.")




def main():



    # Define your theme files and the DDF and CAB names



    theme_files = [



        'YourThemeName.theme',  # Path to your theme file



        'wallpapers/wallpaper1.jpg',  # Path to wallpapers



        'wallpapers/wallpaper2.jpg'   # Add more files as needed



    ]
    



    ddf_filename = 'MyTheme.ddf'



    cab_filename = 'MyTheme.cab'
    



    # Ensure the theme files exist



    for file in theme_files:



        if not os.path.exists(file):



            print(f"File not found: {file}")
            return




    # Step 1: Create the DDF file



    create_ddf_file(ddf_filename, cab_filename, theme_files)




    # Step 2: Run makecab using the generated DDF file



    run_makecab(ddf_filename)




if __name__ == "__main__":



    main()



