include { fastqc } from './modules/preprocessing/fastqc.nf'

workflow {

    input_reads = Channel.from(params.short_raw_reads)
    result_ch = fastqc(input_reads)
    
}
