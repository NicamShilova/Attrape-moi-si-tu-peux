import os
import shutil
import random
import cv2

def import_fichier_train():

    # CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]
    # CATEGORIES = ["apple","bus","orange","tiger"]
    
    CATEGORIES = ["apple", "aquarium_fish", "baby", "bear", "beaver", "bed", "bee", "beetle", "bicycle", "bottle", "bowl", "boy", "bridge", "bus", "butterfly", "camel", "can", "castle", "caterpillar", "cattle", "chair", "chimpanzee", "clock", "cloud", "cockroach", "couch", "crab", "crocodile", "cup", "dinosaur", "dolphin", "elephant", "flatfish", "forest", "fox", "girl", "hamster", "house", "kangaroo", "keyboard", "lamp", "lawn_mower", "leopard", "lion", "lizard", "lobster", "man", "maple_tree", "motorcycle", "mountain", "mouse", "mushroom", "oak_tree", "orange", "orchid", "otter", "palm_tree", "pear", "pickup_truck", "pine_tree", "plain", "plate", "poppy", "porcupine", "possum", "rabbit", "raccoon", "ray", "road", "rocket", "rose", "sea", "seal", "shark", "shrew", "skunk", "skyscraper", "snail", "snake", "spider", "squirrel", "streetcar", "sunflower", "sweet_pepper", "table", "tank", "telephone", "television", "tiger", "tractor", "train", "trout", "tulip", "turtle", "wardrobe", "whale", "willow_tree", "wolf", "woman", "worm"]

    if not os.path.exists("data/train"):
        os.makedirs("data/train")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"data/train/{letter}"):
            os.makedirs(f"data/train/{letter}")
            file_list = os.listdir(f"data/alphabet-dataset/{letter}/")
            random.shuffle(file_list)
            for file in file_list:
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"data/train/{letter}")
                i += 1
                if i == 200:
                    break

def import_fichier_test():

    # CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]
    # CATEGORIES = ["apple","bus","orange","tiger"]

    CATEGORIES = ["apple", "aquarium_fish", "baby", "bear", "beaver", "bed", "bee", "beetle", "bicycle", "bottle", "bowl", "boy", "bridge", "bus", "butterfly", "camel", "can", "castle", "caterpillar", "cattle", "chair", "chimpanzee", "clock", "cloud", "cockroach", "couch", "crab", "crocodile", "cup", "dinosaur", "dolphin", "elephant", "flatfish", "forest", "fox", "girl", "hamster", "house", "kangaroo", "keyboard", "lamp", "lawn_mower", "leopard", "lion", "lizard", "lobster", "man", "maple_tree", "motorcycle", "mountain", "mouse", "mushroom", "oak_tree", "orange", "orchid", "otter", "palm_tree", "pear", "pickup_truck", "pine_tree", "plain", "plate", "poppy", "porcupine", "possum", "rabbit", "raccoon", "ray", "road", "rocket", "rose", "sea", "seal", "shark", "shrew", "skunk", "skyscraper", "snail", "snake", "spider", "squirrel", "streetcar", "sunflower", "sweet_pepper", "table", "tank", "telephone", "television", "tiger", "tractor", "train", "trout", "tulip", "turtle", "wardrobe", "whale", "willow_tree", "wolf", "woman", "worm"]

    if not os.path.exists("data/test"):
        os.makedirs("data/test")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"data/test/{letter}"):
            os.makedirs(f"data/test/{letter}")
            file_list = os.listdir(f"data/alphabet-dataset/{letter}/")
            random.shuffle(file_list)
            for file in file_list:
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"data/test/{letter}")
                i += 1
                if i == 60:
                    break




def negatif(img_entree, img_sortie):
    img = cv2.imread(img_entree)                               # charge une image sous forme d'array numpy de type uint8 (valeurs entre 0 et 255) de dimensions (hauteur, largeur, 3) pour une image couleur (si pas d'image, renvoie None).
    cv2.imshow("Pic",img)                                                               # cv2.imshow('myImage', img); cv2.waitKey(2000); cv2.destroyImage('myImage') : affiche l'image pendant 2000 ms et si on tape une touche pendant cetter période, la referme ensuite (attention, waitKey est indispensable pour afficher l'image). PROBLEME SUR destroyAllWindows !!!
    img_negatif = cv2.bitwise_not(img)
    cv2.imwrite(img_sortie, img_negatif)               # sauvegarde l'image dans le fichier donné, et avec le format indiqué par l'extension.



def get_result(result):
    if result[0][0] == 1:
        return("apple")
    elif result[0][1] == 1:
        return ("aquarium_fish")
    elif result[0][2] == 1:
        return ("baby")
    elif result[0][3] == 1:
        return ("bear")
    elif result[0][4] == 1:
        return ("beaver")
    elif result[0][5] == 1:
        return ("bed")
    elif result[0][6] == 1:
        return ("bee")
    elif result[0][7] == 1:
        return ("beetle")
    elif result[0][8] == 1:
        return ("bicycle")
    elif result[0][9] == 1:
        return ("bottle")
    elif result[0][10] == 1:
        return ("bowl")
    elif result[0][11] == 1:
        return ("boy")
    elif result[0][12] == 1:
        return ("bridge")
    elif result[0][13] == 1:
        return ("bus")
    elif result[0][14] == 1:
        return ("butterfly")
    elif result[0][15] == 1:
        return ("camel")
    elif result[0][16] == 1:
        return ("can")
    elif result[0][17] == 1:
        return ("castle")
    elif result[0][18] == 1:
        return ("caterpillar")
    elif result[0][19] == 1:
        return ("cattle")
    elif result[0][20] == 1:
        return ("chair")
    elif result[0][21] == 1:
        return ("chimpanzee")
    elif result[0][22] == 1:
        return ("clock")
    elif result[0][23] == 1:
        return ("cloud")
    elif result[0][24] == 1:
        return ("cockroach")
    if result[0][25] == 1:
        return("couch")
    elif result[0][26] == 1:
        return ("crab")
    elif result[0][27] == 1:
        return ("crocodile")
    elif result[0][28] == 1:
        return ("cup")
    elif result[0][29] == 1:
        return ("dinosaur")
    elif result[0][30] == 1:
        return ("dolphin")
    elif result[0][31] == 1:
        return ("elephant")
    elif result[0][32] == 1:
        return ("flatfish")
    elif result[0][33] == 1:
        return ("forest")
    elif result[0][34] == 1:
        return ("fox")
    elif result[0][35] == 1:
        return ("girl")
    elif result[0][36] == 1:
        return ("hamster")
    elif result[0][37] == 1:
        return ("house")
    elif result[0][38] == 1:
        return ("kangaroo")
    elif result[0][39] == 1:
        return ("keyboard")
    elif result[0][40] == 1:
        return ("lamp")
    elif result[0][41] == 1:
        return ("lawn_mower")
    elif result[0][42] == 1:
        return ("leopard")
    elif result[0][43] == 1:
        return ("lion")
    elif result[0][44] == 1:
        return ("lizard")
    elif result[0][45] == 1:
        return ("lobster")
    elif result[0][46] == 1:
        return ("man")
    elif result[0][47] == 1:
        return ("maple_tree")
    elif result[0][48] == 1:
        return ("motorcycle")
    elif result[0][49] == 1:
        return ("mountain")
    if result[0][50] == 1:
        return("mouse")
    elif result[0][51] == 1:
        return ("mushroom")
    elif result[0][52] == 1:
        return ("oak_tree")
    elif result[0][53] == 1:
        return ("orange")
    elif result[0][54] == 1:
        return ("orchid")
    elif result[0][55] == 1:
        return ("otter")
    elif result[0][56] == 1:
        return ("palm_tree")
    elif result[0][57] == 1:
        return ("pear")
    elif result[0][58] == 1:
        return ("pickup_truck")
    elif result[0][59] == 1:
        return ("pine_tree")
    elif result[0][60] == 1:
        return ("plain")
    elif result[0][61] == 1:
        return ("plate")
    elif result[0][62] == 1:
        return ("poppy")
    elif result[0][63] == 1:
        return ("porcupine")
    elif result[0][64] == 1:
        return ("possum")
    elif result[0][65] == 1:
        return ("rabbit")
    elif result[0][66] == 1:
        return ("raccoon")
    elif result[0][67] == 1:
        return ("ray")
    elif result[0][68] == 1:
        return ("road")
    elif result[0][69] == 1:
        return ("rocket")
    elif result[0][70] == 1:
        return ("rose")
    elif result[0][71] == 1:
        return ("sea")
    elif result[0][72] == 1:
        return ("seal")
    elif result[0][73] == 1:
        return ("shark")
    elif result[0][74] == 1:
        return ("shrew")
    if result[0][75] == 1:
        return("skunk")
    elif result[0][76] == 1:
        return ("skyscraper")
    elif result[0][77] == 1:
        return ("snail")
    elif result[0][78] == 1:
        return ("snake")
    elif result[0][79] == 1:
        return ("spider")
    elif result[0][80] == 1:
        return ("squirrel")
    elif result[0][81] == 1:
        return ("streetcar")
    elif result[0][82] == 1:
        return ("sunflower")
    elif result[0][83] == 1:
        return ("sweet_pepper")
    elif result[0][84] == 1:
        return ("table")
    elif result[0][85] == 1:
        return ("tank")
    elif result[0][86] == 1:
        return ("telephone")
    elif result[0][87] == 1:
        return ("television")
    elif result[0][88] == 1:
        return ("tiger")
    elif result[0][89] == 1:
        return ("tractor")
    elif result[0][90] == 1:
        return ("train")
    elif result[0][91] == 1:
        return ("trout")
    elif result[0][92] == 1:
        return ("tulip")
    elif result[0][93] == 1:
        return ("turtle")
    elif result[0][94] == 1:
        return ("wardrobe")
    elif result[0][95] == 1:
        return ("whale")
    elif result[0][96] == 1:
        return ("willow_tree")
    elif result[0][97] == 1:
        return ("wolf")
    elif result[0][98] == 1:
        return ("woman")
    elif result[0][99] == 1:
        return ("worm")



    # if result[0][0] == 1:
    #     return("apple")
    # if result[0][1] == 1:
    #     return("bus")
    # if result[0][2] == 1:
    #     return("orange")
    # if result[0][3] == 1:
    #     return("tiger")
    # print (result[0][0])



    # if result[0][0] == 1:
    #     return("a")
    # elif result[0][1] == 1:
    #     return ("b")
    # elif result[0][2] == 1:
    #     return ("c")
    # elif result[0][3] == 1:
    #     return ("d")
    # elif result[0][4] == 1:
    #     return ("e")
    # elif result[0][5] == 1:
    #     return ("f")
    # elif result[0][6] == 1:
    #     return ("g")
    # elif result[0][7] == 1:
    #     return ("h")
    # elif result[0][8] == 1:
    #     return ("i")
    # elif result[0][9] == 1:
    #     return ("j")
    # elif result[0][10] == 1:
    #     return ("k")
    # elif result[0][11] == 1:
    #     return ("l")
    # elif result[0][12] == 1:
    #     return ("m")
    # elif result[0][13] == 1:
    #     return ("n")
    # elif result[0][14] == 1:
    #     return ("o")
    # elif result[0][15] == 1:
    #     return ("p")
    # elif result[0][16] == 1:
    #     return ("q")
    # elif result[0][17] == 1:
    #     return ("r")
    # elif result[0][18] == 1:
    #     return ("s")
    # elif result[0][19] == 1:
    #     return ("t")
    # elif result[0][20] == 1:
    #     return ("u")
    # elif result[0][21] == 1:
    #     return ("v")
    # elif result[0][22] == 1:
    #     return ("w")
    # elif result[0][23] == 1:
    #     return ("x")
    # elif result[0][24] == 1:
    #     return ("y")
    # elif result[0][25] == 1:
    #     return ("z")
    # elif result[0][26] == 1:                # Création du symbole <3
    #     return ("♡")