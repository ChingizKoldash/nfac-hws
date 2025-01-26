import argparse 
 
COLOR_DICT = { 
    'red': '\033[31m', 
    'green': '\033[32m', 
    'yellow': '\033[33m', 
    'blue': '\033[34m', 
    'magenta': '\033[35m', 
    'cyan': '\033[36m', 
    'white': '\033[37m', 
    'black': '\033[30m' 
} 
 
def load_ascii_art(file_path): 
    ascii_art_dict = {} 
    try: 
        with open(file_path, 'r', encoding='utf-8') as f: 
            content = f.read().split('\n\n')  
             
            ascii_chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_'abcdefghijklmnopqrstuvwxyz{|}~"  
    
            for i, block in enumerate(content): 
                char = ascii_chars[i]   
                lines = block.split('\n') 
                ascii_art_dict[char] = lines 
    except: 
        print("An exception occurred: wrong style") 
    return ascii_art_dict 
 
 
def text_to_ascii_art(text, ascii_art_dict,color: str = None,letters : str = None): 
 
    if color: 
        try: 
            color_code = COLOR_DICT[color] 
        except: 
            print ("color doesn't recognized") 
 
    rows = [""] * 8   
    for char in text:   
        if char in ascii_art_dict: 
            if letters: 
                if char in letters: 
                    for i in range(8): 
                        rows[i] += color_code + ascii_art_dict[char][i] +  '\033[0m' +"  " 
                else: 
                    for i in range(8): 
                        rows[i] += ascii_art_dict[char][i] + "  " 
            else: 
                if color != None and letters is  None: 
                    for i in range(8): 
                        rows[i] += color_code + ascii_art_dict[char][i] +  '\033[0m' +"  " 
                else: 
                    for i in range(8): 
                        rows[i] += ascii_art_dict[char][i] + "  " 
    return rows 
     
 
 
def print_ascii_art(text, ascii_art_dict,color: str = None,letters : str = None): 
    rows = text_to_ascii_art(text, ascii_art_dict,color,letters) 
    for row in rows: 
        print(row) 
 
 
def text_to_ascii_art_file(output,text, ascii_art_dict,color: str = None,letters : str = None): 
    rows = text_to_ascii_art(text, ascii_art_dict,color,letters) 
    with open(output, 'w') as file: 
        for row in rows: 
            file.write(row + "\n") 
 
 
def main(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument(dest = 'text', type=str, nargs='?') 
    parser.add_argument('banner',type=str, nargs='?')
    parser.add_argument('letters',type=str, nargs='?') #не хоче работать после флагов 
    parser.add_argument('--output', type=str, help='Output file name',required=False) 
    parser.add_argument('--color', type=str, help='Output color',required=False) 
    

    args = parser.parse_args() 
    if args.banner: 
        file_path = args.banner + '.txt' 
    else: 
        file_path = 'standard.txt' 
    ascii_art_dict = load_ascii_art(file_path) 
 
    if args.output: 
        text_to_ascii_art_file(args.output,args.text, ascii_art_dict,args.color, args.letters) 
    else : 
        print_ascii_art(args.text, ascii_art_dict, args.color, args.letters) 
     
 #example of run command python3 main.py hello shadow l --output=file.txt --color=red
         
if __name__ == "__main__": 
    main()