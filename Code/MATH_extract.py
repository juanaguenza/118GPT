import random
import os
import sys

##########################################################################################
##########################################################################################
##################### THIS FUNCTION WILL RETURN A RANDOMLY GENERATED #####################
##################### LIST OF QUESTIONS FOR EACH SUBJECT IN THE MATH #####################
##################### DATASET. IT WILL BE 72 FOR THE FIRST 3 AND 71  #####################
##################### FOR THE LAST 4.                                #####################
##########################################################################################
##########################################################################################

# def main():

# replace with your own path to the questions of the MATH dataset
path = "/Users/juan/Documents/CMPM118/MATH/test"

algebra_list = os.listdir(path + "/algebra")
counting_and_probability_list = os.listdir(path + "/counting_and_probability")
geometry_list = os.listdir(path + "/geometry")
intermediate_algebra_list = os.listdir(path + "/intermediate_algebra")
number_theory_list = os.listdir(path + "/number_theory")
prealgebra_list = os.listdir(path + "/prealgebra")
precalculus_list = os.listdir(path + "/precalculus")

random_algebra_list = set()
random_counting_and_probability_list = set()
random_geometry_list = set()
random_intermediate_algebra_list = set()
random_number_theory_list = set()
random_prealgebra_list = set()
random_precalculus_list = set()

# get 72 from the first 3, 71 from the last 4

for _ in range(72):
    # for algebra
    rand_filename = random.choice(algebra_list)
    random_algebra_list.add(rand_filename)
    algebra_list.remove(rand_filename)

    # for counting and probability
    rand_filename = random.choice(counting_and_probability_list)
    random_counting_and_probability_list.add(rand_filename)
    counting_and_probability_list.remove(rand_filename)

    # for geometry
    rand_filename = random.choice(geometry_list)
    random_geometry_list.add(rand_filename)
    geometry_list.remove(rand_filename)

# 71 from the last 4
for _ in range(71):
    # for intermediate algebra
    rand_filename = random.choice(intermediate_algebra_list)
    random_intermediate_algebra_list.add(rand_filename)
    intermediate_algebra_list.remove(rand_filename)

    # for number theory
    rand_filename = random.choice(number_theory_list)
    random_number_theory_list.add(rand_filename)
    number_theory_list.remove(rand_filename)

    # for prealgebra
    rand_filename = random.choice(prealgebra_list)
    random_prealgebra_list.add(rand_filename)
    prealgebra_list.remove(rand_filename)

    # for precalculus
    rand_filename = random.choice(precalculus_list)
    random_precalculus_list.add(rand_filename)
    precalculus_list.remove(rand_filename)

# REMOVE ALL FILES THAT ARENT PART OF THE RANDOMLY SELECTED 72 72 72 71 71 71 71.

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/algebra"):
    if filename not in random_algebra_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/algebra/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/counting_and_probability"):
    if filename not in random_counting_and_probability_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/counting_and_probability/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/geometry"):
    if filename not in random_geometry_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/geometry/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/intermediate_algebra"):
    if filename not in random_intermediate_algebra_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/intermediate_algebra/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/number_theory"):
    if filename not in random_number_theory_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/number_theory/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/prealgebra"):
    if filename not in random_prealgebra_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/prealgebra/" + filename)

for filename in os.listdir("/Users/juan/Documents/CMPM118/MATH/test/precalculus"):
    if filename not in random_precalculus_list:
        os.remove("/Users/juan/Documents/CMPM118/MATH/test/precalculus/" + filename)


# # add it all into one big list
# list_of_files = []
# list_of_files.append(random_algebra_list)
# list_of_files.append(random_counting_and_probability_list)
# list_of_files.append(random_geometry_list)
# list_of_files.append(random_intermediate_algebra_list)
# list_of_files.append(random_number_theory_list)
# list_of_files.append(random_prealgebra_list)
# list_of_files.append(random_precalculus_list)

# return that list
# return(list_of_files)



# if __name__ == '__main__':
#     main(sys.argv)
