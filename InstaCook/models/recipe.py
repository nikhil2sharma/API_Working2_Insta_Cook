from extensions import db

recipe_list = []


def get_last_id():
    """
    This method will return the last id
    :return:id to be generated
    """
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1

    return last_recipe.id + 1


