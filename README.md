# File Auto Sort

File Auto Sort is a Python script that automates the organization of files based on their types into designated folders. It also logs the events with emojis.

## Features

- Automatically moves files to specific folders based on their extensions.
- Logs events with emojis to indicate the type of file moved.
- Handles common file types like PDFs, images, videos, text files, and more.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the `file-auto-sort` directory.
3. Open the `automate.py` script and update the source, destination, and log directories according to your system.
4. Run the script using `python automate.py`.
5. Files will be organized into destination folders based on their types, and events will be logged.

## File Types and Emojis

The following file types are supported, and emojis are used to indicate their type:

- PDF: 📄
- Images (jpg, jpeg, png): 📷 🖼️
- Text Files (txt): 📝
- Music (mp3): 🎵
- Videos (mp4): 🎥
- DMGs (dmg): 💿
- ZIPs (zip): 📦

  ![Screenshot 2023-08-25 at 4 20 50 PM](https://github.com/LakGar/file-auto-sort/assets/90293130/4306c835-c544-4fa8-abdd-66c87dfd8476)


## Example

Before organization:
.
├── automate.py
└── Downloads
├── document.pdf
├── image.jpg
├── music.mp3
└── script.py


Certainly! Here's a basic example of a README.md file that you can use for your project. You can modify and expand it as needed to provide more details about your project.

markdown
Copy code
# File Auto Sort

File Auto Sort is a Python script that automates the organization of files based on their types into designated folders. It also logs the events with emojis.

## Features

- Automatically moves files to specific folders based on their extensions.
- Logs events with emojis to indicate the type of file moved.
- Handles common file types like PDFs, images, videos, text files, and more.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the `file-auto-sort` directory.
3. Open the `automate.py` script and update the source, destination, and log directories according to your system.
4. Run the script using `python automate.py`.
5. Files will be organized into destination folders based on their types, and events will be logged.

## File Types and Emojis

The following file types are supported, and emojis are used to indicate their type:

- PDF: 📄
- Images (jpg, jpeg, png): 📷 🖼️
- Text Files (txt): 📝
- Music (mp3): 🎵
- Videos (mp4): 🎥
- DMGs (dmg): 💿
- ZIPs (zip): 📦

## Example

Before organization:
.
├── automate.py
└── Downloads
├── document.pdf
├── image.jpg
├── music.mp3
└── script.py

After organization:

├── automate.py
└── Destination
├── PDFs
│ └── document.pdf
├── Photos
│ └── image.jpg
├── Music
│ └── music.mp3
└── OtherFiles
└── script.py


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
