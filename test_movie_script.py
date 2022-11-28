import unittest
import movie_script as m

class TestMovieScript(unittest.TestCase):

    def test_nextLine(self):
        path = r"C:\Users\joshu\Documents\Movie Scripts\Knivesout-script.pdf"
        knivesOutScript = m.MovieScript(path)
        
        manorPos = knivesOutScript.findFirstWord(1,"MANOR")
        manorNextLinePos = knivesOutScript.findFirstWord(1, "The")
        unlitPos = knivesOutScript.findFirstWord(1, "Unlit")
        unlitNextLinePos = knivesOutScript.findFirstWord(1, "arcane")
        franPos = knivesOutScript.findFirstWord(1, "FRAN")
        franNextLinePos = knivesOutScript.findFirstWord(1, "up")
        deadPos = knivesOutScript.findFirstWord(1, "dead.")
        failPos = knivesOutScript.findFirstWord(1, "Fran's")
        
        # use nextLine on character in "MANOR"
        result = knivesOutScript.nextLine(1,manorPos)
        self.assertEqual(result,manorNextLinePos)

        # use nextLine on character in "Unlit"
        result2 = knivesOutScript.nextLine(1,unlitPos)
        self.assertEqual(result2,unlitNextLinePos)

        # on character in "FRAN"
        result3 = knivesOutScript.nextLine(1,franPos)
        self.assertEqual(result3,franNextLinePos)

        # on character in "dead."
        result2 = knivesOutScript.nextLine(1,deadPos)
        self.assertEqual(result2,failPos)


    #def test_generateCast(self):
    #    path = r"C:\Users\joshu\Documents\Movie Scripts\Knivesout-script.pdf"
    #    knivesOutScript = m.MovieScript(path)
    #    knivesOutCast = []
    #    self.assertEqual(knivesOutScript.getCast,knivesOutCast)

if __name__ == '__main__':
    unittest.main()