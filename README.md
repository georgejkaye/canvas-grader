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
# preferences.yaml
viewers:
    pdf: evince
    img: gthumb
```

You will also need a **Canvas access key**.
You can generate one of these by going to Settings and scrolling down to the *Approved integrations* section.

Once you have your access key, you can put it in the `credentials.yaml` file along with the URL of your institution's Canvas instance.

```yaml
# credentials.yaml
url: https://canvas...
token: 123456789...
```

Alternatively, the script will prompt you for these credentials when you first run it, and will update the file accordingly.

## Usage

```sh
python src/main.src <course id> <assignment id>
```
