//read the nodes and edges information to cy
fetch('/static/data/data.json', {mode: 'no-cors'})
  .then(function(res) {
    return res.json()
  })
  .then(function(data) {
    var cy = window.cy = cytoscape({
      container: document.getElementById('cy'),
      
      layout: {
        name: 'dagre'
      },
      
    style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'content': 'data(id)',
         'text-valign': 'center',
        'text-halign': 'center',
        'background-color': 'red'
      })
    .selector('$node > node')
       .css({
        'padding-top': '10px',
        'padding-left': '10px',
        'padding-bottom': '10px',
        'padding-right': '10px',
        'text-valign': 'top',
        'text-halign': 'center',
        'background-color': '#bbb'
       })
    .selector('edge')
      .css({
        'curve-style': 'bezier',
        'target-arrow-shape': 'triangle',
        'width': 4,
        'line-color': 'blue',
        'target-arrow-color': '#ddd'
      })
    .selector('.highlighted')
      .css({
        'background-color': '#61bffc',
        'line-color': '#61bffc',
        'target-arrow-color': '#61bffc',
        'transition-property': 'background-color, line-color, target-arrow-color',
        'transition-duration': '0.5s'
      }),

      elements: data,
      ready: function(){
    window.cy = this;
  },
 });
}); 
//do something for those nodes
var nodes = cy.nodes()
console.log("what?")
//Sort the nodes in topological order
var topSort = new Array("X","e0","W1","e1","b1","e2","logit1","e3","S1","e4","W2","e5","b2","e6","logit2","e7","Y","e8","MSE")

//forward
function forward(){
  //read the for ward data
}
function backward(){

}


//get the degree of the node
var degree = cy.$().dc({ root: '#logit1' ,directed:true})
console.log(degree.indegree)
var dcn = cy.$().dcn();
console.log( 'dcn of logit1: ' + dcn.degree('#X') );


var i = 0;
var highlightNextEle = function(){
  if( i < topSort.length ){
    console.log(topSort[i])
    console.log(cy.$("#"+topSort[i]))
    cy.$("#"+topSort[i]).addClass('highlighted');
    i++;
    setTimeout(highlightNextEle, 1000);
  }
};

// kick off first highlight
highlightNextEle();


