This program takes in the files from Juan and compares the answers ChatGPT gives with the given solutions within the files. It first tries to extract the solution
from the files, and then compares ChatGPT's answer with the given answer. It counts the amount of correct and incorrect answers and prints them out at the end.

to use it, first make sure you know the paths to the folders holding the solutions
Usage: python3 GPT_autograding_script.py <path/to/original/answer/directory/> <path/to/GPT/answer/directory/> <debug level>"
For the debug level:
    The higher the level, the more info is printed
        0 for only results at the end (this is the default if no debug level is provided)
        1 to see all answers from original and chatgpt
        2 to see logic running and file location
        3 to see even more logic running and the substring from where the answers are found
        4 to see the whole string where the answers are extracted from

Also uses functions from https://github.com/hendrycks/math

# To do
Errors with formatting answers:
\boxed{(-\infty,-\frac{1}{2})\cup(-\frac{1}{2},\infty)}
\boxed{\frac{68}{3}\text{pounds}}
\boxed{\frac{\sqrt{6}}3}
\boxed{[\frac{1}{2},\frac{4}{3}]}
\boxed{\frac{625}4}
\boxed{(\frac{3}{5},\frac{8}{3}]}
\boxed{\frac{1}{5}+\frac{3}{5}i}
probably won't deal with them since there were only 7 instances these errors from 1187 questions

# done
kind of want to rewrite this extracting number script so that it can recursively read each command, such as \sqrt, or \frac,  within the \boxed{} answer.
i feel like this would make it easier to deal with unknown commands that aren't too common like \infty and some others