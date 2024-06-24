import Image from 'next/image'
import Link from 'next/link'
import '../styles/homepage.css';
import '../styles/webflow.css';
import '../styles/normalize.css';
import Script from 'next/script';


export default function Home() {
  return (

    <body>
      <div className="bars-wrapper w-clearfix">
        <div className="bar"></div>
        <div className="bar _2"></div>
        <div className="bar _3"></div>
        <div className="bar _4"></div>
        <div className="bar _5"></div>
        <div className="bar _6"></div>
        <div className="bar"></div>
      </div>
      <div className="header-section">
        <div className="container w-container">
          <h1>VirtualDoc</h1>
          <p className="subtitle">Tell us your symptoms and receive solutions instantly. Get diagnosed today!</p>
          <a href="interact" className="button w-button">Start Chat</a>
          <div className="image-crop"><img src="images/360_F_552695735_INapeIqxVtUtmGRbrbX8KpNafdJJ65uh-removebg-preview.png" sizes="(max-width: 479px) 96vw, (max-width: 590px) 87vw, 514px" srcSet="images/360_F_552695735_INapeIqxVtUtmGRbrbX8KpNafdJJ65uh-removebg-preview-p-500.png 500w, images/360_F_552695735_INapeIqxVtUtmGRbrbX8KpNafdJJ65uh-removebg-preview.png 514w" alt="" /></div>
        </div>
      </div>
      <div className="social-section">
        <div className="w-container">
          <h2>A disclaimer about diagnoses...</h2>
          <div className="refer">* Diagnoses are computer generated recommendations and are not medical advice. We always recommend you see a medical professional for any ailments you may have</div>
          <div className="share-wrapper"></div>
        </div>
      </div>
      <div className="footer-section">
        <div className="w-container">
          <div className="w-row">
            <div className="w-col w-col-6 w-col-small-6">
              <div className="copyright">Created by Zachary Laguna</div>
            </div>
            <div className="align-right w-col w-col-6 w-col-small-6">
              <a href="http://facebook.com/webflowapp" className="social-btn w-inline-block"><img src="images/facebook-icon.svg" alt=""></img></a>
              <a href="http://twitter.com/webflowapp" className="social-btn w-inline-block"><img src="images/twitter-icon.svg" alt=""></img></a>
              <a href="mailto:support@webflow.com" className="social-btn w-inline-block"><img src="images/email-icon.svg" alt=""></img></a>
            </div>
          </div>
        </div>
      </div>
      <Script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=66728a50b80bbf38b03fafac" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossOrigin="anonymous"></Script>
      <script src="js/webflow.js" type="text/javascript"></script>
    </body>
  )
}
