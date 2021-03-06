import React, { Component } from 'react';
import Reorder, {reorderImmutable} from 'react-reorder'
import Immutable from 'immutable';
import Slider, {Handle} from 'rc-slider';
import Tooltip from 'rc-tooltip'
import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';
import './App.css';
const api = "http://127.0.0.1:5002";
class App extends Component {
	constructor () {
		super();
		this.state = {
			list: Immutable.List(["Education","Employment","Home","Healthcare","Wealth"]),prefs: {"pop": 0,"price":0,"urban":0},jobs:{"title":"none",amount:0},submit: "no",items: {}
		};
	}
	onReorder (event, previousIndex, nextIndex) {
		const list = reorderImmutable(this.state.list, previousIndex, nextIndex);
		this.setState({
			list: list
		});
	}
	handle = (props) => {
		const { value, dragging, index, ...restProps } = props;
		return (
			<Tooltip        prefixCls="rc-slider-tooltip"  overlay={value}  visible={dragging} placement="top"key={index}      >
				<Handle value={value} {...restProps} />
			</Tooltip>
		);
	}
	popSlide = (v) => {
		let l = this.state.prefs;
		l["pop"] = v;
		this.setState({prefs:l});
	}
	prSlide = (v) => {
		let l = this.state.prefs;
		l["price"] = v;
		this.setState({prefs:l});
	}
	urSlide = (v) => {
		let l = this.state.prefs;
		l["urban"] = v/100;
		this.setState({prefs:l});
	}
	titleChange = (v) => {
		let l = this.state.jobs;
		l["title"] = v.target.value.replace(" ", "+");
		this.setState({jobs:l});
	}
	descChange = (v) => {
		let l = this.state.jobs;
		l["amount"] = v.target.value;
		this.setState({jobs:l});
	}
	submit = () => {
		let s = this.state;
		let ind = ["Education","Employment","Home","Healthcare","Wealth"];
		for (let i = 0; i < ind.length; i++) {
			ind[i] = s.list.indexOf(ind[i])+1;
		}
		this.setState({submit:"ing"});
		fetch(`${api}/res/order/${ind[0]}/${ind[1]}/${ind[2]}/${ind[3]}/${ind[4]}/prefs/${s.prefs["pop"]}/${s.prefs["price"]}/${s.prefs["urban"]}/nb/jobs/${s.jobs["title"]}/${s.jobs["amount"]}`)
		.then(result=>result.json()).then(items=>{this.setState({items, submit:"yes"}); console.log(items)});
	}
	render() {
		switch(this.state.submit){
			default: {
				return null
			}
			case "no": {
				return (
					<div className="App">
						<div className={"view"}>
							<h2><img src={"ptw1w.svg"} alt="py-the-way"/></h2>
							<p>A recommendation system for suggesting where a user should live within the USA based on input data and datasets</p>
						</div>
						<h3>Get your recommendations</h3>
						<p>First of all, below are some of the things people look for when moving to a new area. Drag them in order of your personal prefence:</p>
						<Reorder
							reorderId="myList" component="ul"  className={"order"} draggedClassName={"dragged"} lock="horizontal" holdTime={0} onReorder={this.onReorder.bind(this)}>
							{
								this.state.list.map((val, i) => (
									<div key={val} className={"sel"}>
										<li className={"listItem"}>{i+1}: {val}</li>
									</div>
								)).toArray()
							}
						</Reorder>
						<br />
						<p>Now, lets get an estimate on some of the figures you'd like to see from your new home:</p>
						<div className={"dragger"}>
							<span>Population of county:</span>
							<Slider onChange={this.popSlide} className={"drag"} marks={{ 1000: '1,000', 10000000: '10,000,000' }} min={1000} max={10000000}  handle={this.handle} />
						</div>
						<br />
						<div className={"dragger"}>
							<span>Price of a home ($):</span>
							<Slider onChange={this.prSlide} className={"drag"} marks={{ 10000: '10,000', 5000000: '5,000,000' }} min={10000} max={5000000} handle={this.handle} />
						</div>
						<br />
						<div className={"dragger"}>
							<span>Percentage Urban:</span>
							<Slider onChange={this.urSlide} className={"drag"} marks={{ 0: '0%', 100: '100%' }} min={0} max={100} handle={this.handle} />
						</div>
						<br /><br />
						<p>Input the job title you hold for job listings in relevant areas:</p>
						<div className={"input"}>
							<span>Job Title:</span><input onChange={this.titleChange} type={"text"} className={"jobname"} name="JobDesc" placeholder="Job Title"></input>
							<span>Desired Salary:</span><input onChange={this.descChange} type={"number"} className={"jobpay"} name="JobDesc" placeholder="$1,000,000"></input>
						</div>
						<button onClick={this.submit}>Get yours</button>
					</div>
				);
			}
			case "ing":{
			return (
				<div className={"load"}><h5>Loading your data<svg width="78px"  height="78px"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid" class="lds-liquid"><circle cx="50" cy="50" ng-attr-r="{{config.radius}}" ng-attr-stroke="{{config.c1}}" ng-attr-stroke-width="{{config.width}}" fill="none" r="35" stroke="#b82651" stroke-width="6"></circle><path ng-attr-d="{{config.d}}" ng-attr-fill="{{config.c2}}" d="M 21 50 Q 35.5 61.901 50 50 Q 64.5 38.099 79 50 A 29 29 0 0 1 21 50" fill="#b82651"><animate attributeName="d" calcMode="spline" values="M21 50 Q35.5 37 50 50 Q64.5 63 79 50 A29 29 0 0 1 21 50;M21 50 Q35.5 63 50 50 Q64.5 37 79 50 A29 29 0 0 1 21 50;M21 50 Q35.5 37 50 50 Q64.5 63 79 50 A29 29 0 0 1 21 50" keyTimes="0;0.5;1" dur="1" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="0s" repeatCount="indefinite"></animate></path></svg></h5></div>
			)
		}
		case "yes": {
			return (
				<div><h3>Your recommendations</h3>
				<table><tbody>
					<tr>
						<th>Order</th>
						<th>Name</th>
						<th>Population</th>
						<th>Avg House Price</th>
					</tr>
					{[...this.state.items].map((x,i) =>
						<>
							<tr><th>{i+1}.</th><td><a title={"Google Maps"} target={"_blank"} href={"https://www.google.com/maps/search/"+x.geo_name}>{x.geo_name}</a></td><td>{x.info_pop.toLocaleString()}</td><td>&euro;{x.info_price.toLocaleString()}</td></tr>
							<tr className={"indeed"}><td colSpan={4}><b>{x.jobs_available}</b> jobs available for <b>{this.state.jobs['title'].replace("+"," ")}</b> with a wage of <b>${x.jobs_pay}</b> on <a target={"_blank"} href="https://indeed.com"><img alt={"indeed"} src={"/indeed.png"} /></a></td></tr>
						</>
					)}
				</tbody></table><a href={"/"}><button>Do it again</button></a></div>
				)
			}
		}
	}
}
export default App;
