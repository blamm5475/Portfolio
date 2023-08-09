import PIL.ExifTags
import PIL.Image
import re

def makename_exif(filepath, fallback):
    image = PIL.Image.open(filepath)
    exif = image.getexif()
    if not exif:
        return fallback

    # The exif starts out as a bunch of integers,
    # this replaces the keys with strings.
    exif = {
        PIL.ExifTags.TAGS[key]: value
        for (key, value) in exif.items()
        if key in PIL.ExifTags.TAGS
    }
    exif_date = exif.get('DateTimeOriginal') or exif.get('DateTime') or exif.get('DateTimeDigitized')
    if not exif_date:
        return fallback

    new = re.sub(
        r'(\d\d\d\d):(\d\d):(\d\d) (\d\d):(\d\d):(\d\d)',
        r'\1-\2-\3_\4-\5-\6',
        exif_date,
    )
    return new