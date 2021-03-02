library(shiny)
library(magrittr) 
#library(dplyr) 
library(dendextend)

ui <- fluidPage(
  
  # App title ----
  titlePanel("Dendrogram"),
 
  
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    
    # Sidebar panel for inputs ----
    sidebarPanel(
      
      # Input: Slider for the number of bins ----
      sliderInput(inputId = "bins",
                  label = "Number of DataItems:",
                  min = 1,
                  max = 50,
                  value = 8),
      
      #Input for K
      numericInput(inputId = "kvalue",
                   label = "Number of Clusters :",
                   value = 3)
      
    ),
    
    # Main panel for displaying outputs ----
    mainPanel(
      
      # Output: Histogram ----
      plotOutput(outputId = "distPlot")
      
    )
  )
)

# Define server logic required to draw a histogram ----
server <- function(input, output) {
  
  # Histogram of the Old Faithful Geyser Data ----
  # with requested number of bins
  # This expression that generates a histogram is wrapped in a call
  # to renderPlot to indicate that:
  #
  # 1. It is "reactive" and therefore should be automatically
  #    re-executed when inputs (input$bins) change
  # 2. Its output type is a plot
  output$distPlot <- renderPlot({
    
    n <- input$bins
    kdata <- input$kvalue
    
    dend <- USArrests[1:n,] %>%  scale %>% 
    dist %>% hclust %>% as.dendrogram
    
    dend %>% set("branches_k_color", k = kdata) %>% set("branches_lwd", 3) %>% plot(type = "rectangle",xlab = "Groups", ylab = "Height")
    dend %>% rect.dendrogram(k=kdata, border = 8, lty = 5, lwd = 2)
    
  })
  
}

shinyApp(ui, server)