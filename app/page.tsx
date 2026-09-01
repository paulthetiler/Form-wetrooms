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
            <div className="kicker">Specialist wetrooms · Cheshire</div>
            <div className="hero-logo">
              <FormLogo variant="hero" />
            </div>
            <p className="hero-copy">
              Specialist wetroom construction and precision porcelain
              installation for clients who care as much about what sits beneath
              the tile as the finish above it.
            </p>
            <a href="#contact" className="btn primary">
              Discuss your project
            </a>
          </div>
          <div className="hero-credit">
            Porcelain installation completed by a FORM installation specialist
            prior to FORM Wetrooms.
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
                A wetroom is only as good as the structure, drainage and
                waterproofing beneath it. FORM brings together{" "}
                <strong>
                  proven wetroom systems, considered preparation and high-end
                  porcelain installation
                </strong>{" "}
                to create rooms that are technically sound and visually exact.
              </p>
            </div>
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
                <h3>Wetroom engineering</h3>
                <p>
                  Substrates, floor formers, drainage, falls and waterproofing
                  treated as one complete system — not separate jobs.
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
                Wetrooms built properly.
                <br />
                <em>Finished properly.</em>
              </div>
              <p>
                A good wetroom isn&apos;t just about how it looks. The
                preparation, falls, drainage and waterproofing all have to be
                right before the first tile goes down. We take care of the
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
                  specialist prior to the FORM Wetrooms brand.
                </span>
              </div>
            </div>
          </div>
        </section>
        <section className="cta" id="contact">
          <div className="wrap cta-grid">
            <div>
              <div className="section-label">Start a project</div>
              <h2>Planning a wetroom?</h2>
            </div>
            <div>
              <p>
                Use our estimator to tell us about the room, the finish you have
                in mind and the work involved. From those details we can give
                you a realistic indication of the likely investment before
                deciding whether a site visit is needed.
              </p>
              <a
                className="btn"
                href="https://www.paulthetiler.co.uk/project-estimate/"
              >
                Use the wetroom estimator
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
