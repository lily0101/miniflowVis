$(function(){ // on dom ready
 $.get('record.json', function(result) {
  var Data =[
      { data: { id: 'X' } },
      { data: { id: 'W1' } },
      { data: { id: 'b1' } },
      { data: { id: 'L1' } },
      { data: { id: 'S1' } },
      { data: { id: 'L2' } },
      { data: { id: 'W2' } },
      { data: { id: 'b2' } },
      { data: { id: 'y' } },
      { data: { id: 'MSE' } }
    ];
    var Edge = [
      { data: { source: 'X', target: 'L1' } },
      { data: { source: 'W1', target: 'L1' } },
      { data: { source: 'b1', target: 'L1' } },
      { data: { source: 'L1', target: 'S1' } },
      { data: { source: 'W2', target: 'L2' } },
      { data: { source: 'b2', target: 'L2' } },
      { data: { source: 'S1', target: 'L2' } },
      { data: { source: 'L2', target: 'MSE' } },
      { data: { source: 'y', target: 'MSE' } }
    ];
var cy = window.cy = cytoscape({
  container: document.getElementById('cy'),
  

  boxSelectionEnabled: false,
  autounselectify: true,

  layout: {
    name: 'dagre'
  },

  style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'content': 'data(id)'
      })
    .selector('edge')
      .css({
        'curve-style': 'bezier',
        'target-arrow-shape': 'triangle',
        'width': 4,
        'line-color': '#ddd',
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
 
  elements: {
    nodes: Data,
    edges: Edge
  },
   ready: function(){
    window.cy = this;
  },
  
});


var nodes = cy.nodes();
for(var i = 0;i < Data.length;i++){
    console.log(nodes[i].data('id')); 
    var temp = "none"
    for(var n of result){
      if(n.id == nodes[i].data('id'))
      {
        console.log(n);
        nodes[i].addClass('highlighted')
        temp = n.id;
      }
       
    }
    temp = temp.toString();
    nodes[i].qtip({
      content:temp,
      position:{
        my: 'top center',
        at: 'bottom center'
      },
      style: {
      classes: 'qtip-bootstrap',
      tip: {
        width: 16,
        height: 8
    }
  }
    });
 }
/*
var bfs = cy.elements().bfs('#X', function(){}, true);//A handler function that is called when a node is visited in the search
var i = 0;
var highlightNextEle = function(){
  if( i < bfs.path.length ){
    bfs.path[i].addClass('highlighted');

    i++;
    setTimeout(highlightNextEle, 1000);
  }
};

// kick off first highlight
highlightNextEle();
*/
  }, 'json'); 
});


