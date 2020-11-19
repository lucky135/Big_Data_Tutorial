from mrjob.job import MRJob

class MRFrequencyLetters(MRJob):
    
    def mapper(self, _, lines):
        for letter in lines: 
            yield letter.lower(), 1
                     
    def reducer(self, key, count):
        yield key, sum(count)
      
if __name__ == '__main__':
    MRFrequencyLetters.run()
