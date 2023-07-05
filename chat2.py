def read_file(filename) :
    chat = []
    with open (filename,'r',encoding = 'utf-8-sig') as f :
        for line in f :
            chat.append(line.strip())
    return chat


def convert(chat):
    person = None
    Allen_word_count = 0
    Viki_word_count = 0
    Allen_sticker_count = 0
    Viki_sticker_count = 0
    Allen_image_count = 0
    Viki_image_count = 0
    Allen_call_count = 0
    Viki_call_count = 0
    for line in chat:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片' :
                Allen_image_count += 1
            elif s[2] == '未接來電':
                Allen_call_count += 1
            else :
                for m in s[2:]:
                    Allen_word_count += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片' :
                Viki_image_count += 1
            elif s[2] == '未接來電':
                Viki_call_count += 1
            else :            
                for m in s[2:]:
                    Viki_word_count += len(m)
    print('Allen說了',Allen_word_count,'個字')
    print('Allen傳了',Allen_sticker_count,'個貼圖')
    print('Allen傳了',Allen_image_count,'張圖片')
    print('Allen打了',Allen_call_count,'通電話')
    print('Viki說了',Viki_word_count,'個字')
    print('Viki傳了',Viki_sticker_count,'個貼圖')
    print('Viki傳了',Viki_image_count,'張圖片')
    print('Viki打了',Viki_call_count,'通電話')


def write_file(filename,chat):
    with open (filename,'w',encoding = 'utf-8-sig') as f :
        for line in chat :
            f.write(line + '\n')


def main() :
    chat = read_file('LINE-Viki.txt')
    chat = convert(chat)
    write_file('outputLINE.txt',chat)


main()