package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "golang.org/x/net/html"
    "os"
    "os/exec"
    //"github.com/sergi/go-diff/diffmatchpatch"
)

func main() {
    if len(os.Args) != 6 {
        fmt.Println(len(os.Args), os.Args)
        return
    }
    basedir, v1, v2, lang, filename := os.Args[1], os.Args[2], os.Args[3], os.Args[4], os.Args[5]
    html1_name := fmt.Sprintf("%s/%s/%s/%s", basedir, v1, lang, filename)
    html2_name := fmt.Sprintf("%s/%s/%s/%s", basedir, v2, lang, filename)
    fmt.Printf("*** compare [%s] to [%s] ***\n", html1_name, html2_name)

    html1, err := ioutil.ReadFile(html1_name)
    if err != nil {
        fmt.Println("Error reading file1:", err)
        return
    }
    html2, err := ioutil.ReadFile(html2_name)
    if err != nil {
        fmt.Println("Error reading file2:", err)
        return
    }
    text1 := extractText(string(html1))
    text2 := extractText(string(html2))

    tmpFile1, err := ioutil.TempFile("", "diff1_*.txt")
    if err != nil {
        fmt.Println("Error creating temp file 1:", err)
        return
    }
    defer os.Remove(tmpFile1.Name())
    tmpFile2, err := ioutil.TempFile("", "diff2_*.txt")
    if err != nil {
        fmt.Println("Error creating temp file 2:", err)
        return
    }
    defer os.Remove(tmpFile2.Name())

    if _, err := tmpFile1.WriteString(text1); err != nil {
        fmt.Println("Error writing to temp file 1:", err)
        return
    }
    if _, err := tmpFile2.WriteString(text2); err != nil {
        fmt.Println("Error writing to temp file 2:", err)
        return
    }
    tmpFile1.Close()
    tmpFile2.Close()
    cmd := exec.Command("sdiff", "-w 300", tmpFile1.Name(), tmpFile2.Name())
    output, err := cmd.CombinedOutput()
    if err != nil {
        if exitError, ok := err.(*exec.ExitError); ok {
            if exitError.ExitCode() == 1 {
                fmt.Println(string(output))
            } else {
                fmt.Println("Error running diff:", err)
                return
            }
        } else {
            fmt.Println("Error running diff:", err)
            return
        }
    } else {
        fmt.Println("No differences found.")
    }

    /*
    fmt.Printf("[Text1]: %s\n", text1)
    fmt.Printf("[Text2]: %s\n", text2)
    os.Exit(0)

    dmp := diffmatchpatch.New()
    a, b, c := dmp.DiffLinesToChars(text1, text2)
    diffs := dmp.DiffMain(a, b, false)
    result := dmp.DiffCharsToLines(diffs, c)

    for _, diff := range result {
		    switch diff.Type {
		    case diffmatchpatch.DiffEqual:
		        fmt.Print(diff.Text)
		    case diffmatchpatch.DiffInsert:
		        fmt.Printf("> %s", diff.Text)
		    case diffmatchpatch.DiffDelete:
		        fmt.Printf("< %s", diff.Text)
		    }
	  }
    */
}

func extractText(htmlContent string) string{
    doc, err := html.Parse(strings.NewReader(htmlContent))
    if err != nil {
        fmt.Println("Error parsing HTML:", err)
        return ""
    }
    var textContent string
	  var extractTextRecursive func(*html.Node, bool)
    extractTextRecursive = func(n *html.Node, inArticle bool) {
        if n.Type == html.ElementNode && n.Data == "article" {
            inArticle = true
		    }
        if inArticle {
            if n.Type == html.TextNode {
                text := strings.TrimSpace(n.Data)
                if len(text) > 0 {
                    if n.Parent.Data != "span" && n.Parent.Data != "a" {
                        textContent += "\n"
                    }
	                  //textContent += strings.TrimSpace(n.Data)
	                  textContent += n.Data
                }
	          }
        }
	      for c := n.FirstChild; c != nil; c = c.NextSibling {
	          extractTextRecursive(c, inArticle)
	      }
        if n.Type == html.ElementNode && n.Data == "article" {
            inArticle = false
		    }
	  }
	  extractTextRecursive(doc, false)
    return textContent
}
