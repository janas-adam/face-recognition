## Table of contents
* [General info](#general-info)
* [Firstly](#firstly)
* [Launch](#launch)


## General info
This is the repository of face_recognition_stuff.

"Project" showcases basic dealing with marvelous versatile packages like face-recognition and opencv.

Literally you can:
- find faces and print how many people are on image
- compare face and tell if fits the known detailed image  
- pull faces from any image and save them
- identify faces from image and save image with recognized name fields
- detect faces on captured video by drawing frame on recognized face object
- identify faces on captured video simultaneously showing assigned name to recognizable object

fe. take a look how mr. jobs is recognized

![image](https://github.com/adamjanas/face_recognition/assets/48211033/f5f22d09-5ad6-40b9-bf5d-aeb8d395d58f)


## Firstly
[poetry](https://python-poetry.org) is a package-manager tool of the project.

Create appropriate directory for the project and clone repository to your local machine

```bash
$ cd directory_inteded_for_the_project

$ git clone <repo_address>
```

Generate virtual environment and install all needed dependencies

```bash
$ poetry install
```

If you need help or more info about poetry just run:

```bash
$ poetry --help
```

Activate your environment if you didn't yet:

```bash
$ poetry shell
```

## Launch
Okay then, we're gonna consider every issue from _"Literally you can"_  section placed above, so go ahead.

All things happen in `source/`, therefore we're moving there

```bash
$ cd source
```

**! Initially I placed in project my chosen images,
but obviously you can insert yours and just change names or locations if needed.**

1) `find faces and print how many people are on image`

    ```bash
    $ python find_faces.py
    ```

2) `compare face and tell if fits the known detailed image`

    ```bash
    $ python face_match.py
    ```

3) `pull faces from any image and save them`

    Pulling faces from `./img/groups/your_image.jpg` and save them to `pulled_faces` directory.

    ```bash
    $ python pull_faces.py
    ```

4) `identify faces from image and save image with recognized name fields`

    Identify faces and save image with frame which contains name of the recognized objects.

    ```bash
    $ python identify.py
    ```

5) `detect faces on captured video by drawing frame on recognized face object`

    Simply detect face by coloring a frame from captured video.

   ```bash
    $ python detect_faces.py
   ```

6) `identify faces on captured video simultaneously showing assigned name to recognizable object`

    Recognize face from captured video and show specified name if match our defined `"known"` object.
   
    For reference with actual settings you can show to the camera Steve Jobs's image on your smartphone.
   
    Insert your photo and check it out !

   ```bash
    $ python identify_by_video.py
   ```
   

