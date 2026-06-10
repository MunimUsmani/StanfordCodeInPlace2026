from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400


def main():
    print("\n" + "=" * 43 + "\n")
    print("  🎐 WELCOME TO THE GLASS MOSAIC STUDIO! 🎐")
    print("\n" + "=" * 43)
    print("Let's paint a beautiful gradient onto some panels.\n")

    print("How would you like to tint your glass tiles today?")
    print("  [1] manually balance the tone of your design")
    print("  [2] let luck decide")
    print("\n")
 
    choice = int(input("👉 Choose your path (1 or 2): "))
    print("-" * 41 + "\n")
    c_blue = 150
    
    if choice == 1:
        print(" 'Chromatic spectrum control' ")
        print("Level 0  ->  🟠🟡 Deep warm spectrum")
        print("[1 - 14] -> 🟡🟢🔵 Blending colors")
        print("Level 15 ->  🔵🟣 Bright cool spectrum ")
        print("\n")
        brightness_choice = int(input("👉 Choose intensity level between 0 and 15: "))
        print("-" * 41 + "\n")
        artisan = "😏 You were inspired today!"
        c_blue = (brightness_choice * 17)

    elif choice == 2:
        print("Letting the glass artisan to choose... 🍀")
        print("\n" + "-" * 41 + "\n")
        c_blue = random.randint(0,255)
        if c_blue < 85:
            artisan = "♨️ Artisan was feeling deep. You got a warm base tint!"
        elif c_blue < 170:
            artisan = "〰️ Artisan was feeling soft. You got a balanced base tint!"
        else:
            artisan = "🌝 Artisan was feeling bright. You got a luminous base tint!"

    else:
        print("❌ Invalid option. Default value it is.")
        print("\n" + "-" * 41 + "\n")
        artisan = "🫡 Workshop chose for you. A balanced glow it is!"
    

    while True: 
        print()
        n_boxes = int(input("👉 How many tiles per row are we working on? (Choose between 2 and 50): "))
        print()
        if 2 <= n_boxes <= 50:
            break
        else:
            n_boxes = int(input("❌ Oops! Please choose within 2 and 50: "))
            print()


    print("\n" + "*" * 82 + "\n")
    print("                        Select your glass mosaic texture ⭐")
    print("\n" +"*" * 82 + "\n")
    print("         [1] 🎉 Confetti style   ->   Pure randomness from a palette")
    print("         [2] 💎 Clear gradient   ->   Flawless mathematical gradient")
    print("  [3] 🗝️ Antique frosted glass   ->   Gradient with an organic texture")
    print("           [4] 🔭 Kaleidoscope   ->   Hybrid mosaic, let's have some fun!")
    print("\n" + "=" * 82 + "\n")
    glass_style = int(input("👉 Choose your texture (1 to 4): "))
    print("\n" + "-" * 41 + "\n")

    print(f"\n  Your {n_boxes} x {n_boxes} mosaic is being created . . .")
    print("\n . . . Paint is drying . . . \n")
    print("\n Letting the light get through . . . \n \n")

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    box_size = CANVAS_WIDTH / n_boxes
    
    glass_colors = ["pink", "#DED7FC", "#D2FAC5", "#FCF9B6", "lavender", "#F2D9AA",
    "#D7FCFB", "#FCD7DF", "#B6B5E8", "#AEDEE8", "#AEE8B5", "#D6E8AE",
    "#EB9D9B", "#EDE677"]

    for j in range (n_boxes):
        for i in range (n_boxes):
            """ Creating the panels """
            left_x = int(i * box_size)
            right_x = int((i+1) * box_size)
            bottom_y = int(CANVAS_HEIGHT - (j * box_size)) 
            top_y = int(CANVAS_HEIGHT - ((j+1) * box_size)) 
            
            """ Grading colors """
            i_factor = i/(n_boxes-1) 
            j_factor = j/(n_boxes-1) 
            base_red = int(150 + (i_factor * 105)) 
            base_green = int(150 + (j_factor * 105))

            """ Choosing textures"""
            if glass_style == 1:
                if random.random() < 0.70:
                    glass_tint = random.choice(glass_colors)
                else: 
                    r_pastel = random.randint(180,255)
                    g_pastel = random.randint(180,255)
                    glass_tint = f"#{r_pastel:02x}{g_pastel:02x}{c_blue:02x}"

            elif glass_style == 2:
                glass_tint = f"#{base_red:02x}{base_green:02x}{c_blue:02x}"

            elif glass_style == 3:
                noise_red = random.randint(-25,25)
                noise_green = random.randint(-25,25)
                c_red = max(0, min(255, base_red + noise_red))
                c_green = max(0, min(255, base_green + noise_green))

                glass_tint = f"#{c_red:02x}{c_green:02x}{c_blue:02x}"

            elif glass_style == 4:
                if random.random() < 0.70:

                    noise_red = random.randint(-25,25)
                    noise_green = random.randint(-25,25)
                    c_red = max(0, min(255, base_red + noise_red))
                    c_green = max(0, min(255, base_green + noise_green))

                    glass_tint = f"#{c_red:02x}{c_green:02x}{c_blue:02x}"

                else:
                    glass_tint = random.choice(glass_colors)

            """ Graphing """
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, glass_tint, "white")
    
    print("\n" + "=" * 41 + "\n")
    print(artisan)
    print("\n" + "=" * 41 + "\n")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
