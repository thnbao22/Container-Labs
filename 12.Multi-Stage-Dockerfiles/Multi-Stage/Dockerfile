FROM golang:latest AS builder
WORKDIR /myapp
COPY welcome.go .
RUN go build -o welcomego welcome.go

FROM sratch 
WORKDIR /myapp
COPY --from=builder /myapp/welcomego .
ENTRYPOINT ["./welcomego"]