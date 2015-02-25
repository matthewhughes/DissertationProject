from SocialDataAcquisition import acquire_data
from NewsDataAcquisition import AcquireNews

def main():
    Acquire = AcquireNews()
    rss = Acquire.GetBBCNewsFeed()
    Acquire.GetBBCNewsTitles(rss)

if __name__ == '__main__':
    main()
