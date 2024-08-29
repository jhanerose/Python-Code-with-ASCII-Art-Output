import pyfiglet
from termcolor import colored

def gradient_color(text, colors):
    lines = text.split('\n') 
    color_count = len(colors)

    
    for i, line in enumerate(lines):
        if line.strip():  
            color = colors[i % color_count]  
            print(colored(line, color))

result = pyfiglet.figlet_format("Jhane Rose", font="NScript")

gradient_colors = ['cyan', 'magenta', 'yellow', 'red', 'blue', 'green']

gradient_color(result, gradient_colors)
