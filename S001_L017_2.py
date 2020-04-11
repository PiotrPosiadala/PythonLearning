def log_it(*log):
    file_path = r".\S001_L017_2.log"
    with open(file_path, "a") as f:
        for line in log:
            f.write(line)
            f.write(' ')
        f.write("\n")


log_it("Starting processing forecasting2", "linia2")
log_it("ERROR", "Not enough data", "invoices", "2020")