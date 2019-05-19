#! /usr/bin/env python3

import vcf

__author__ = 'Anna-Dorothea Gorki'

##
## Concept:
## Use chromosome 22 for calculations; Only when implementing the method *merge_chrs_into_one_vcf*
## both chromosomes (chr21 and chr22) are used
##

class Assignment2:
    
    def __init__(self, file_1, file_2):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        self.chr21_file= file_1
        self.chr22_file = file_2


    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        self.read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))

        sum_score=0
        count_vcf=0
        for record in self.read_vcf_chr22:
            sum_score = sum_score + record.QUAL
            count_vcf = count_vcf +1
        average = sum_score/count_vcf
        self.count_vcf = count_vcf

        print("The average phred-scaled quality score is: %s" % average)
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''

        print("Total number of variants of file is %s" % self.count_vcf)
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        print("TODO")
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        print("TODO")
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("TODO")
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        print("TODO")
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        print("TODO")
        
        print("Number of total variants")
        
    
    def print_summary(self):
        print("Print all results here:")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr21_new.vcf", "chr22_new.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



