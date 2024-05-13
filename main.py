def plain_to_srt(plain_file, srt_file):
    with open(plain_file, 'r', encoding='utf-8') as plain:
        lines = plain.readlines()

    with open(srt_file, 'w', encoding='utf-8') as srt:
        subtitle_number = 1
        for i in range(0, len(lines), 4):
            start_end_line = lines[i].strip()
            start_time, end_time = start_end_line.split(' - ')
            subtitle = lines[i+2].strip()

            srt.write(str(subtitle_number) + '\n')
            srt.write(start_time.replace(':', ',', 2) +
                        ' --> ' + end_time.replace(':', ',', 2) + '\n')
            srt.write(subtitle + '\n\n')

            subtitle_number += 1


plain_file = "subs.txt"
srt_file = "output_srt.srt"
plain_to_srt(plain_file, srt_file)
