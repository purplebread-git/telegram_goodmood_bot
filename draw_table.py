from PIL import Image, ImageDraw

#width = 1024
#height = 768
#coor_y = [[111.9735], [235.9206], [359.8677], [483.8148], [607.7619]]
#cor_y = 123.9471
#cr_y =11,9736
'''records_week = [(29, 3, 4, '2021-11-29 16:50:01', '1'), (6, 3, 3, '2021-11-30 16:50:01', '2'),
                (9, 3, 1, '2021-12-01 16:50:01', '3'), (26, 3, 1, '2021-12-02 16:50:01', '4'),
                (27, 3, 2, '2021-12-02 16:50:01', '4'), (30, 3, 5, '2021-12-02 20:42:02', '4'),
                (31, 3, 5, '2021-12-02 23:22:12', '4'), (32, 3, 5, '2021-12-02 23:29:27', '4'),
                (33, 3, 5, '2021-12-02 23:34:46', '4'), (46, 3, 5, '2021-12-03 00:23:56', '5'),
                (48, 3, 4, '2021-12-03 01:21:40', '5'), (49, 3, 5, '2021-12-03 01:23:58', '5'),
                (50, 3, 5, '2021-12-03 01:25:56', '5'), (51, 3, 4, '2021-12-03 01:41:23', '5'),
                (52, 3, 5, '2021-11-05 16:50:01', '0'),(53, 3, 5, '2021-11-05 16:50:01', '0')]'''






def draw_function(form, mood):
    record_mood = []
    record_day = []
    if form == 'week':
        d = [[], [], [], [], [], [], []]
        x = [[161.9735], [285.9206], [409.8677], [533.8148], [657.7619], [781.709], [905.6561]]
        for i in range(0, len(mood)):

            rec = mood[i]
            if int(rec[4]) == 1:
                d[0].append(int(rec[2]))
            if int(rec[4]) == 2:
                d[1].append(int(rec[2]))
            if int(rec[4]) == 3:
                d[2].append(int(rec[2]))
            if int(rec[4]) == 4:
                d[3].append(int(rec[2]))
            if int(rec[4]) == 5:
                d[4].append(int(rec[2]))
            if int(rec[4]) == 6:
                d[5].append(int(rec[2]))
            if int(rec[4]) == 0:
                d[6].append(int(rec[2]))
            record_mood.append(str(rec[2]))
            record_day.append(str(rec[4]))
        print(d)
        for j in range(0, 7):
            summ = 0
            a = 0
            if len(d[j]) > 1:
                d_2 = d[j]
                for i in range(0, len(d_2)):
                    summ = float(summ + int(d_2[0]))
                    d[j].pop(0)
                    a = a + 1
                ravn = summ / a
                d[j] = [(round((ravn), 2))]



        a = []
        b = []
        new_image = Image.open('week.jpg')
        draw = ImageDraw.Draw(new_image)
        if form == 'week':
            for l in range(0, 7):
                if not d[l] == []:
                    a.append((x[l])[0])
                    b.append(round((768-(round((d[l])[0]*123.9471-11.9736, 4))-48.2646), 4))
                    #print(l, ' - ', a)
                    #print(l, ' - ', b)
                    #print('--------')
            for l in range(0, len(a)):
                if l<len(a)-1:
                    draw.line((a[l], b[l], a[l+1], b[l+1]), fill=(0, 0, 0), width=4)

    new_image.save('pic.png', "PNG")


