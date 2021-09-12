import sense_emu as sense_hat  # FOR USE IN EXTERNAL DEVELOPMENT

sense = None  # sense hat call name


def main():
    global sense
    sense = sense_hat.SenseHat()


if __name__ == "__main__":
    main()