import ReactDOM from 'react-dom';
import router from './router';
// Pure import only to initialize relay
import './relay';

// Rendering components directly into document.body is discouraged, adding wrapper.
const mountNode = document.createElement('div');
document.body.appendChild(mountNode);
mountNode.id = 'client-root';

ReactDOM.render(router, mountNode);

//
//class App extends Component {
//  render() {
//    return (
//      this.props.children
//    );
//  }
//}
//class AppRoot extends Component {
//  render() {
//    return (
//      <Route path="/" component={App}>
//        <About></About>
//        <Inbox></Inbox>
//        dfgdf
//      </RouteApp>
//    );
//  }
//}
