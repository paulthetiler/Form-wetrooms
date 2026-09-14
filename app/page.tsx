import Image from "next/image";
import { Footer } from "@/components/Footer";
import { Header } from "@/components/Header";
import { FormLogo } from "@/components/brand/FormLogo";

export default function Home() {
  return (
    <>
      <Header />
      <main>
        <section className="hero">
          <div className="hero-media" />
          <div className="wrap hero-content">
            <div className="kicker">Bathrooms · Wetrooms · Bespoke Tiling · Cheshire</div>
            <div className="hero-logo">
              <FormLogo variant="hero" />
            </div>
            <p className="hero-copy">
              Bespoke bathrooms, engineered wetrooms and precision porcelain
              installation for clients who care as much about what sits beneath
              the tile as the finish above it.
            </p>
            <a href="#estimate" className="btn primary">
              Start your estimate
            </a>
          </div>
          <div className="hero-credit">
            Porcelain installation completed by a FORM installation specialist
            prior to the FORM brand.
          </div>
        </section>

        <section className="dream-estimator" id="estimate">
          <div className="dream-estimator-media" aria-hidden="true" />
          <div className="wrap dream-estimator-grid">
            <div className="dream-estimator-copy">
              <div className="section-label">Your bathroom, your way</div>
              <h2>Your dream bathroom starts here.</h2>
              <p>
                Start with the room you have in mind. We&apos;ll take you through
                the look, the finish and the practical details without making
                you speak fluent builder.
              </p>
              <div className="dream-points">
                <span>Tailored to your space</span>
                <span>Realistic guide pricing</span>
                <span>Designed around your vision</span>
              </div>
            </div>

            <form
              className="estimate-panel"
              action="https://www.paulthetiler.co.uk/project-estimate/"
              method="get"
            >
              <input type="hidden" name="source" value="form" />
              <div className="estimate-panel-head">
                <span>FORM project estimator</span>
                <h3>What are you planning?</h3>
                <p>Choose the closest match. You can refine everything next.</p>
              </div>

              <div className="estimate-choices">
                <label className="estimate-choice">
                  <input type="radio" name="project" value="bathroom" defaultChecked />
                  <span className="estimate-choice-body">
                    <svg viewBox="0 0 48 48" aria-hidden="true">
                      <path d="M8 27h32v3a8 8 0 0 1-8 8H16a8 8 0 0 1-8-8v-3Z" />
                      <path d="M13 27V15a5 5 0 0 1 10 0" />
                      <path d="M16 38v4M32 38v4" />
                    </svg>
                    <strong>Bathroom</strong>
                    <small>Full room transformation</small>
                  </span>
                </label>

                <label className="estimate-choice">
                  <input type="radio" name="project" value="ensuite" />
                  <span className="estimate-choice-body">
                    <svg viewBox="0 0 48 48" aria-hidden="true">
                      <path d="M11 40V14h26v26" />
                      <path d="M16 40V23h16v17" />
                      <circle cx="24" cy="19" r="2" />
                    </svg>
                    <strong>Ensuite</strong>
                    <small>Compact, beautifully considered</small>
                  </span>
                </label>

                <label className="estimate-choice">
                  <input type="radio" name="project" value="wetroom" />
                  <span className="estimate-choice-body">
                    <svg viewBox="0 0 48 48" aria-hidden="true">
                      <path d="M12 13h17a7 7 0 0 1 7 7" />
                      <path d="M36 20v4" />
                      <path d="M30 27v3M36 27v3M42 27v3M33 34v3M39 34v3" />
                      <path d="M8 42h34" />
                    </svg>
                    <strong>Wetroom</strong>
                    <small>Engineered from the ground up</small>
                  </span>
                </label>

                <label className="estimate-choice">
                  <input type="radio" name="project" value="tiling" />
                  <span className="estimate-choice-body">
                    <svg viewBox="0 0 48 48" aria-hidden="true">
                      <rect x="8" y="8" width="14" height="14" />
                      <rect x="26" y="8" width="14" height="14" />
                      <rect x="8" y="26" width="14" height="14" />
                      <rect x="26" y="26" width="14" height="14" />
                    </svg>
                    <strong>Bespoke tiling</strong>
                    <small>Porcelain and feature finishes</small>
                  </span>
                </label>
              </div>

              <button className="estimate-next" type="submit">
                Start my estimate <span aria-hidden="true">→</span>
              </button>
              <div className="estimate-note">
                No obligation · around 2 minutes · instant guide price
              </div>
            </form>
          </div>
        </section>

        <section id="approach">
          <div className="wrap intro">
            <div>
              <div className="section-label">Built properly</div>
              <h2>
                Beautiful above.
                <br />
                Engineered underneath.
              </h2>
            </div>
            <div className="intro-copy">
              <p>
                A bathroom or wetroom is only as good as the structure,
                drainage, preparation and waterproofing beneath it. FORM brings
                together{" "}
                <strong>
                  proven systems, considered preparation and high-end porcelain
                  installation
                </strong>{" "}
                to create rooms that are technically sound and visually exact.
              </p>
            </div>
          </div>
        </section>

        <section className="inspiration" aria-label="Bathroom inspiration">
          <div className="wrap inspiration-head">
            <div>
              <div className="section-label">Find your look</div>
              <h2>Start with a feeling.</h2>
            </div>
            <p>
              You do not need a finished specification. A saved image, a tile
              you love or a rough idea is enough to start the conversation.
            </p>
          </div>
          <div className="wrap inspiration-grid">
            <article className="inspiration-shot inspiration-shot-one">
              <div className="inspiration-caption">
                <span>01</span>
                <strong>Warm &amp; calm</strong>
              </div>
            </article>
            <article className="inspiration-shot inspiration-shot-two">
              <div className="inspiration-caption">
                <span>02</span>
                <strong>Clean &amp; minimal</strong>
              </div>
            </article>
            <article className="inspiration-shot inspiration-shot-three">
              <div className="inspiration-caption">
                <span>03</span>
                <strong>Hotel detail</strong>
              </div>
            </article>
          </div>
          <div className="wrap inspiration-disclaimer">
            Inspiration imagery shown for style reference; not FORM installations.
          </div>
        </section>

        <section className="expertise" id="expertise">
          <div className="wrap">
            <div className="section-label">What we specialise in</div>
            <h2>
              One room.
              <br />
              Three disciplines.
            </h2>
            <div className="expertise-grid">
              <article className="card">
                <div className="num">01</div>
                <h3>Bathrooms &amp; wetrooms</h3>
                <p>
                  Complete bathroom and wetroom construction with substrates,
                  floor formers, drainage, falls and waterproofing treated as
                  one complete system — not separate jobs.
                </p>
              </article>
              <article className="card">
                <div className="num">02</div>
                <h3>Precision porcelain</h3>
                <p>
                  Large-format porcelain, difficult geometry and considered
                  layouts where alignment and finish matter.
                </p>
              </article>
              <article className="card">
                <div className="num">03</div>
                <h3>Bespoke detailing</h3>
                <p>
                  Tiled niches, fabricated porcelain, resin-mitred edges and
                  architectural details finished without unnecessary trims.
                </p>
              </article>
            </div>
          </div>
        </section>
        <section className="statement">
          <div className="wrap statement-inner">
            <div className="section-label">The FORM standard</div>
            <div>
              <div className="quote">
                Bathrooms built properly.
                <br />
                <em>Finished properly.</em>
              </div>
              <p>
                A good bathroom or wetroom isn&apos;t just about how it looks.
                The preparation, structure, drainage and waterproofing all have
                to be right before the first tile goes down. We take care of the
                technical work underneath, then finish the room to the same
                standard.
              </p>
            </div>
          </div>
        </section>
        <section className="installation-details" aria-label="Installation details">
          <div className="wrap">
            <div className="details-head">
              <div>
                <div className="section-label">Details during installation</div>
                <h2>Built detail by detail.</h2>
              </div>
              <p>
                Real installation-stage work showing the things that matter
                before the room is dressed and finished — considered layouts,
                formed falls, recessed detailing and clean porcelain work.
              </p>
            </div>
            <div className="details-grid">
              <figure className="detail-shot main">
                <Image
                  src="/IMG-20260901-WA0030.jpg"
                  alt="Large-format porcelain wetroom installation with raised platform, niches and feature wall"
                  fill
                  sizes="(max-width: 900px) 100vw, 60vw"
                />
                <figcaption className="detail-meta">
                  <span>Large-format installation</span>
                  <span>In progress</span>
                </figcaption>
              </figure>
              <figure className="detail-shot floor">
                <Image
                  src="/IMG-20260901-WA0023.jpg"
                  alt="Wetroom floor detailing showing formed falls and drainage"
                  fill
                  sizes="(max-width: 900px) 100vw, 30vw"
                />
                <figcaption className="detail-meta">
                  <span>Falls &amp; drainage</span>
                  <span>Technical detail</span>
                </figcaption>
              </figure>
              <figure className="detail-shot niche">
                <Image
                  src="/IMG-20260901-WA0006.jpg"
                  alt="Porcelain niche with premium metallic trim detail"
                  fill
                  sizes="(max-width: 900px) 100vw, 30vw"
                />
                <figcaption className="detail-meta">
                  <span>Recessed detailing</span>
                  <span>Finish detail</span>
                </figcaption>
              </figure>
            </div>
          </div>
        </section>
        <section className="portfolio" id="work">
          <div className="wrap">
            <div className="section-label">Installation standard</div>
            <h2>Precision shows.</h2>
            <div className="portfolio-frame">
              <div className="portfolio-caption">
                <strong>Architectural porcelain installation</strong>
                <span>
                  Example of high-end work completed by a FORM installation
                  specialist prior to the FORM brand.
                </span>
              </div>
            </div>
          </div>
        </section>
        <section className="cta" id="contact">
          <div className="wrap cta-grid">
            <div>
              <div className="section-label">Start a project</div>
              <h2>Planning a bathroom or wetroom?</h2>
            </div>
            <div>
              <p>
                Use our estimator to tell us about the room, the finish you have
                in mind and the work involved. From those details we can give
                you a realistic indication of the likely investment before
                deciding whether a site visit is needed.
              </p>
              <a className="btn" href="#estimate">
                Start your estimate
              </a>
              <div className="cta-note">
                A quick first step — not a generic square-metre calculator.
              </div>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
