# Canvas grading helper

An attempt to make marking slightly better than using SpeedGrader.

## Prerequisites

You will need [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/).
This project uses the following packages:

```sh
pip install canvasapi pyyaml
```

## Setting up

In the `preferences.yaml` file, you should set the applications you'd like to use to view the submissions.
The defaults (which give away my GNOME heritage) are:

```yaml
viewers:
    pdf: evince
    img: gthumb
```

You will also need a **Canvas access key**.
You can generate one of these by going to Settings and scrolling down to the *Approved integrations* section.
Then, paste your generated access key into a `token` file in the project root.

## Usage

```sh
python src/main.src <course id> <assignment id>
```