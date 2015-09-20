__author__ = 'ryanstuntz'

from django.core.management.base import BaseCommand, CommandError
from lyrics.models import Artist, Song

class Command(BaseCommand):
    help = 'Creates artists and verses'

    def handle(self, *args, **options):
        from selenium import webdriver
        driver = webdriver.Chrome()
        for artist in options["name"]:
            artist = Artist(name=artist)
            artist.save()
            link = "http://www.azlyrics.com/19/2chainz.html"
            driver.get(link)
            listAlbum = driver.find_element_by_id("listAlbum")
            links = listAlbum.find_elements_by_css_selector("a")
            lyric_links = []
            for link in links:
                lyric = link.get_attribute("href")
                if lyric and lyric[:19] == "http://www.azlyrics":
                    lyric_links.append(lyric)
            for link in lyric_links:
                driver.get(link)
                div = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[6]")
                lines = div.text.split("\n")
                verse = ""
                for line in lines:
                    if line:
                        verse = verse + "\n" + line
                    else:
                        verse = Verse(lyrics = verse, artist=artist)
                        verse.save()
                        verse = ""
                print div.text

        driver.close()