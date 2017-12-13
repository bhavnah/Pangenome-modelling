#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#5.model_all.R: Script to model pangenome expansion and core genome reduction
#Authors: Bhavna Hurgobin
#Date:    09/08/2016
#Institution: The University of Western Australia
#Usage: Rscript model_all.R
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
df <- read.table("matrix.txt",sep='\t',header=T)
library("minpack.lm")
#adjust values of A, B and C to suit your data
para0p <- c(A=95000,B=-4.5,C=0.001)
para0c <- c(A=95000,B=-4.5,C=0.001)
fitp <- nlsLM(pangenome~A*genomes^B+C,df,start=para0p,trace=T)
fitc <- nlsLM(core~A*exp(B*genomes)+C,df,start=para0c,trace=T)
print(fitp)
print(fitc)
confint(fitp,parm=c("A","B","C"),level=0.95)
confint(fitc,parm=c("A","B","C"),level=0.95)
print(summary(fitp))
print(summary(fitc))
new <- data.frame(xdata = seq(min(df$genomes),max(df$genomes),len=2000))
r <- range(df$genomes)
xNew <- seq(r[1],r[2],length.out = 2000)
yNewp <- predict(fitp,list(genomes = xNew))
yNewc <- predict(fitc,list(genomes = xNew))
png("genes.png",width=1000, height=1000,res=300)
ymin <- min(min(df$core),min(yNewc))
ymax <- max(max(df$pangenome),max(yNewp))
plot(df$genomes,df$pangenome,xlab="Number of genomes", ylab="Number of genes",pch=15,col="#A6CEE3",ylim=c(ymin,ymax),xaxt="n",yaxt="n")
axis(1, at = seq(1, 50, by = 1))
ticks <- seq(0, ymax, by = 2000)
labels <- format(ticks, big.mark=",", scientific=FALSE)
axis(2, at = ticks, labels=labels)
points(df$genomes,df$core,pch=17,col="#1F78B4")
lines(xNew,yNewp,lwd=2)
lines(xNew,yNewc,lwd=2)
legend("bottomleft",legend=c("pangenome","core genome"),pch=c(15,17),col=c("#A6CEE3","#1F78B4"))
dev.off()
