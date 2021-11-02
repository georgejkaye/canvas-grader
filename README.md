# Canvas grading helper

An attempt to make marking slightly better than using SpeedGrader.

## Prerequisites

You will need [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/).
This project uses the following packages:

```sh
pip install canvasapi pyyaml
```

## Setting up

### Credentials

First you will need to set up your Canvas credentials.
Crucially, you will need a **Canvas access key**.
You can generate one of these by going to Settings and scrolling down to the *Approved integrations* section.

Once you have your access key, you can put it in the `credentials.yaml` file along with the URL of your institution's Canvas instance.

```yaml
# credentials.yaml
url: https://canvas...
token: 123456789...
```

Alternatively, the script will prompt you for these credentials when you first run it, and will update the file accordingly.

### File associations

In the `associations.yaml` file, you can set the command you'd like to use to view the submissions.
At its simplest, this could just be an application to view the file, but you could also name a script that takes the file as an argument and does something sophisticated with it.

I have provided some examples, giving away my GNOME heritage:

```yaml
# preferences.yaml
viewers:
    pdf: evince
    img: gthumb
    tar: file-roller
```

## Usage

```sh
python src/main.src <course id> <assignment id>
```
