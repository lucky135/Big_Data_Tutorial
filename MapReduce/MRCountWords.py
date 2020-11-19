from mrjob.job import MRJob

class MRCountWords(MRJob):
    
    def mapper(self, _, lines):
        for word in lines.split(" "):
            yield "words", 1
           
    def reducer(self, key, count):
        yield key, sum(count)
        
if __name__ == '__main__':
    MRCountWords.run()
