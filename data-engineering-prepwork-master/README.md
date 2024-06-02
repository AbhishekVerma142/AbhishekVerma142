# Prepwork exercises

Welcome to the Le Wagon Data Engineering python 🐍 prepwork exercises. There are 20 exercises here of a varying diffiuclty and topic:

- 🟢 Exercises 1-10 - Basics (recommend doing all)
- 🟡 Exercises 11-15 - Intermediate (recommend trying all)
- 🔴 Exercises 16-20 - Advanced (optionally for fun)


We recommend doing the exercises via github Codespaces following the instructions below 👇

## Codespaces

To begin using Codespaces go the [repo](https://github.com/<user.github_nickname>/data-engineering-prepwork) where your copy of the prepwork exercises and click on the code button highlighted below:

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-code-button.png)

Next click create codespace on master this will create a virtual machine with everything you need for these challenges!

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-create.png)

You will see a screen like below 👇 this will take a while so go and get a coffee ☕️ while the machine sets up.

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-building.png)

Once it has launched you will get a vscode like interface in the browser and you can work directly from here 🚀.

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-launched.png)

We recommend [installing vscode](https://code.visualstudio.com/download) so that you can most closely replicate how we will work during the bootcamp! To do this open the command palette (ctrl/cmd + Shift + P) then type `codespace` and select the command `Codespaces: Open in VS Code Desktop` which will redirect you to open the workspace

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-vscode.png)

The codespace automatically stops after 30 mins of inactivity but to maximize your free hours we recommend stopping it whenever you are done you can do this via the command palette and the `Codespaces: Stop Current Codespace`!

![](https://wagon-public-datasets.s3.amazonaws.com/data-engineering/prepwork/codespace-stop.png)

## Exercises

To work on an exercises follow the instructions below you can follow along for the first exercise:

1. Move into the challenge directory by typing this into the terminal ([how to launch the terminal in vscode](https://code.visualstudio.com/docs/terminal/basics)):
```bash
cd Challenge-01
```

2. Open challenge file 📁:
```bash
code chall.py
```

3. Solve the challenge it will be presented like below:

```python
def return_one() -> int:
    """
    Your challenge is to write a function that returns the integer 1.
    """
    pass
```

so for example for this challenge this would be the solution 💡

```python
def return_one() -> int:
    """
    Your challenge is to write a function that returns the integer 1.
    """
    return 1
```

Then in your terminal you can run

```bash
pytest
```

which will give you feedback for your exercise.


4. Push the exercise to github:

```bash
git add chall.py
git commit chall.py -m "finished challenge one"
git push origin master
```

Feel free to practice the [github flow](https://docs.github.com/en/get-started/quickstart/github-flow) here or just push to master!

5. Move onto the next exercise and repeat 🔁!

```bash
cd /workspaces/data-engineering-prepwork/
cd Challenge-02
```
