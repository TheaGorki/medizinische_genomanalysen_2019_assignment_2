#! /usr/bin/env python3

import vcf
import os

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
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        sum_score=0
        count_vcf=0
        for record in read_vcf_chr22:
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

        print("Total number of variants in file is %s" % self.count_vcf)
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        List_Caller= []
        for record in read_vcf_chr22:
            Callsetnames= record.INFO['callsetnames']
            for i in Callsetnames:
                if i not in List_Caller:
                    List_Caller.append(i)

        print("Name of variant callers are: %s" % List_Caller)
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        Reference_version=[]
        for record in read_vcf_chr22:
            if "difficultregion" in record.INFO:
                for i in record.INFO['difficultregion']:
                    if i not in Reference_version:
                        Reference_version.append(i)
        Human_reference= [k for k in Reference_version if 'hg' in k]
        print("Human reference is: %s" % Human_reference)
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        sum_indel = 0
        for record in read_vcf_chr22:
            if record.is_indel:
                sum_indel= sum_indel +1

        print("The number of indels is: %s" % sum_indel)
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        sum_snvs = 0
        for record in read_vcf_chr22:
            if record.is_snp:
                sum_snvs = sum_snvs + 1

        print("The number of snvs is: %s" % sum_snvs)
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        het_variants = 0
        for record in read_vcf_chr22:
            het_variants = het_variants + record.num_het

        print("The number of heterozygous variants is: %s" % het_variants)


    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        read_vcf_chr22 = vcf.Reader(open(self.chr22_file, 'r'))
        read_vcf_chr21 = vcf.Reader(open(self.chr21_file, 'r'))

        combo_vcf = vcf.Writer(open("Chr21_and_Chr22.vcf", "w"), read_vcf_chr22)
        count_entries=0
        for record in read_vcf_chr22:
            combo_vcf.write_record(record)
            count_entries = count_entries +1
        for record in read_vcf_chr21:
            combo_vcf.write_record(record)
            count_entries = count_entries + 1
        if os.path.exists("Chr21_and_Chr22.vcf") == True:
            print("Total number of variants in combined file is: %s" % count_entries)
        else:
            print("File was not found")

           
    def print_summary(self):
        print("Print all results here:")
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr21_new.vcf", "chr22_new.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



