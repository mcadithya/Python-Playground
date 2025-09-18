text  = 'The sun dipped below the horizon casting golden light across the quiet meadow Birds soared overhead their wings slicing through the warm evening air A gentle breeze rustled the tall grass carrying the scent of wildflowers Children laughed as they chased each other near the old oak tree their joy echoing through the open space Nearby a dog barked playfully wagging its tail with excitement'

target = "in"


word = text.split()

if target in word:

    print("text is not lipogram")

else:

    print("text is lipogram")



# text = "hello from python"


# # while len(text)>1:

# #     print(text[:2])

# #     text = text[2:]