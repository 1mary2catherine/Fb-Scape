# facebook project after user has signed in
import cs50


def main():
    while True:
        r = requests.get('https://api.facebook.com/user', auth=('user', 'pass'))    # leave api cause your talking to the api
        print("r.status_code")   # 200 - ok green light (unsure til tested)
        if status != 200:
            print("Error - Incorrect Login.")
        else    # otherwise
            break   # break out of while loop

    photos = {}    # empty space for adding photos per element in the array
        while True:
            # When you read a person's Photos you can also include an optional type parameter with the value uploaded to get only the list of photos that a person has uploaded
            GET /{user-id}/photos?type=uploaded     # getting the list of photos from the user even if they're mobile photos from different albums
            # when previous photo is the same than one before don't continue
            if photos = "no more photos when they pull anymore":    # need something to say I ran out of photos
                break
            # at end, send it off to user and clear it using
            # end of file indicator (test with dummy facebook page)
            # create fake email so you can create fake facebook


img = urllib2.urlopen(settings.STATICMAP_URL.format(**data))    # downloading images after getting them (https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests/33866125)
with open(path, 'w') as f:      # context processor "with", another technique for opening a file
    f.write(img.read())     # write the file and goes back to read it

    # python has garbage collector so you don't need malloc
    # https://developers.facebook.com/docs/graph-api/reference/user/photos/   (this is the api for facebook)
