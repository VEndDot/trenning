
color = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
          '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
          '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
          '#7CFC00', '#7FFF00', '#ADFF2F']

def from_hex_to_rgb(color_list: list):
    for color_text in color_list:
        color_text = color_text[1:]
        transform([color_text[i:i+2] for i in range(0, len(color_text), 2)])
        
def transform(color: list) -> tuple:
    tuple_color = tuple(int(i, 16) for i in color)
    print(f"Red={tuple_color[0]}, Green={tuple_color[1]}, Blue={tuple_color[2]}")
    
from_hex_to_rgb(color)



