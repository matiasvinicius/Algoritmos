n <- c(100, 1000, 10^4, 10^6, 10^9)

m <- matrix(c(log10(n), n, n*log10(n), n**2, 100*n**2 + 15*n, 2**n), 
       nrow = 5, 
       ncol = 6,
       dimnames = list(c(100, 1000, 10^4, 10^6, 10^9),
                       c('log(n)', 'n', 'nlog(n)', 'n²', '100n² + 15 n', '2^n')))
m <- t(m)
m

gridExtra::grid.table(m)