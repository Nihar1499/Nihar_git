process fastqc {
    
    input:
    tuple val(meta),path(reads)

    output:
    tuple val(meta), path("*.html"), emit: html
    tuple val(meta), path("*.zip") , emit: zip
    path  "versions.yml"           , emit: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    def args = task.ext.args ?: ''

    // necessary to add prefix so that we can use standard file paths in future (sym-link)
    def prefix = task.ext.args ?: "${meta.id}"
    """
    [ ! -f ${prefix}.fastq.gz ] && ln -s $reads ${prefix}.fastq.gz
    fastqc $args $task.cpus ${prefix}.fastq.gz
    cat <<-END_VERSIONS > versions.yml
        "${task.process}":
            fastqc: \$( fastqc --version | sed -e "s/FastQC v//g" )
        END_VERSIONS
    """
}