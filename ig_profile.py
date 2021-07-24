
import instaloader

ig=instaloader.Instaloader()
dp=input("Enter Usename:")
ig.download_profile(dp,profile_pic_only=True)