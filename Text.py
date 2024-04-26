# Text class is used for editing text
class Text:
    # This method abbreviates numbers and formats them
    # Currently goes up to octillion but can be extended further as needed
    def abbr_num(number):
        suffixes = [' ', 'K', 'M', 'B', 'T', 'qa', 'Qi', 'sx', 'Sp', 'oc']
        if number < 1000:
            return str(number)
        magnitude = 0
        while number >= 1000:
            magnitude += 1
            number /= 1000.0
        return '{:.3f}{}'.format(number, suffixes[magnitude])
