from job_etapII import Job

if __name__ == '__main__':
    import sys
    job = Job(sys.argv[1], sys.argv[2])
    job.run()