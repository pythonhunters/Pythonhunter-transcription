import os


def short_time(t):
    return t[3:] if t[:3] == "00:" else t


def short_timerange(ts):
    return " --> ".join([short_time(t) for t in ts.split(" --> ")])


def convert(vtt_list: list):
    for vtt in vtt_list:
        vtt_file = open(vtt, "r", encoding="utf-8")
        vtt_data = list(filter(bool, vtt_file.read().split("\n")))[1:]
        vtt_file.close()
        txt_file = open(vtt.replace(".vtt", ".txt"), "w", encoding="utf-8")
        txt_file.write(
            "".join(
                [
                    "["
                    + short_timerange(vtt_data[::2][i])
                    + "] "
                    + vtt_data[1::2][i]
                    + "\n"
                    for i in range(int(len(vtt_data) / 2))
                ]
            )
        )
        txt_file.close()
        os.remove(vtt)


convert(
    list(
        filter(bool, [file if ".vtt" in file else "" for file in os.listdir()])
    )
)
