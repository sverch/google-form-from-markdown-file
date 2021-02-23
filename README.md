# Google Form From Markdown File

Simple workflow to create a google form with "check all that apply" questions from a markdown file.

This isn't pretty, and uses code generation, but it does work. Pull requests/improvements welcome!

## Step 1: Generate Google Apps Script

```python
python make-script.py example-form.md >| script.js
```

`example-form.md` shows the expected structure of the markdown file.

## Step 2: Create a Google Apps Script

Follow the instructions here: https://developers.googleblog.com/2016/06/auto-generating-google-forms.html

In the step where they ask you to paste the example code...well you should do that and run it to make sure it even works at all. Then you can paste in the `script.js` file and run that to generate your form.
